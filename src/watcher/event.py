"""Module for EventHandler (deals with event from watchdog)."""
from argparse import Namespace
from subprocess import Popen, run
import time

from watchdog.events import FileSystemEventHandler, FileSystemEvent


class EventHandler(FileSystemEventHandler):
    """Class for handling file system modification events.

    Args:
        params (Namespace, required): parameters from command line.
    """

    def __init__(self, params: Namespace) -> None:
        self.params = params
        self.last_trigger = time.time()
        self.command = self.get_command(params.test, params.lint, params.lint_threshold)
        self.runner = self.get_runner(params.test, params.lint, params.file)
        self.executable = self.get_executable(
            params.dir,
            params.file,
            params.lint,
            params.lint_src
        )
        self.process = None

    def on_modified(self, event: FileSystemEvent) -> None:
        """Execute every modification event.

        Args:
            event (FileSystemEvent): event from file system.
        """
        if self.should_trigger(event):
            run('clear', shell=True, check=False)
            print(f'Event type: {str(event.event_type).upper()}')
            print(f'Path : {event.src_path}')
            print(f'Running {self.runner}...')

            if self.process is not None:
                self.process.kill()

            with Popen(f'{self.command} {self.executable}', shell=True) as process:
                self.process = process
                self.last_trigger = time.time()

    def should_trigger(self, event: FileSystemEvent) -> bool:
        """Test whether it should trigger for the event.

        Args:
            event (FileSystemEvent): event information.

        Returns:
            status (bool): True if it should trigger, False otherwise.
        """
        # Test whether the timeout is over
        delta = time.time() - self.last_trigger
        time_criteria = delta > self.params.time

        # Test whether the location should be changed
        locations = ['.git']
        location_criteria = not any(map(event.src_path.__contains__, locations))

        file_types = ['swp']
        type_criteria = not any(map(event.src_path.__contains__, file_types))

        return all([time_criteria, location_criteria, type_criteria])

    def get_runner(self, test: bool, lint: bool, file_to_execute: str) -> str:
        """Which name should be displayed when running.

        Args:
            test (bool): if it should run pytest.
            lint (bool): if it should run pylint.
            file_to_execute (str): name of the file to execute.

        Returns:
            runner (str): name to display.
        """
        if test:
            return "pytest"
        if lint:
            return "pylint"
        return file_to_execute

    def get_command(self, test: bool, lint: bool, lint_threshold: float) -> str:
        """Selects which command it should run.

        Args:
            test (bool): if it should run pytest.
            lint (bool): if it should run pylint.

        Return:
            command (str): which command it should run.
        """
        if test:
            return "pytest"
        if lint:
            if lint_threshold is not None:
                return f"pylint --fail-under={lint_threshold}"
            return "pylint"
        return "python"

    def get_executable(
        self,
        directory: str,
        file_to_execute: str,
        lint: bool,
        lint_src: str
    ) -> str:
        """Builds string to execute.

        Args:
            directory (str): the directory it is looking
            file_to_execute (str): file that it should run.
            lint (bool): if it should run pylint.
            lint_src (str): where the lint should be run.

        Returns:
            executable (str): complete command to execute.
        """
        executable = ""
        if directory is not None:
            executable += f"{directory}/"
        if file_to_execute is not None:
            executable += file_to_execute
        if lint:
            return lint_src
        return executable
