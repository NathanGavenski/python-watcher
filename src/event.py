"""Module for EventHandler (deals with event from watchdog)."""
from argparse import Namespace
import time
import os

from watchdog.events import FileSystemEventHandler, FileSystemEvent


# TODO event from VS Code and vim are different
class EventHandler(FileSystemEventHandler):
    """Class for handling file system modification events."""

    def __init__(self, params: Namespace) -> None:
        self.params = params
        self.last_trigger = time.time()
        self.command = self.get_command(params.test)
        self.executable = self.get_executable(params.dir, params.file)

    def on_modified(self, event: FileSystemEvent) -> None:
        """Execute every modification event.

        Args:
            event (FileSystemEvent): event from file system.
        """
        if 'swp' not in event.src_path and self.should_trigger():
            os.system('clear')
            print(f'Event type: {str(event.event_type).upper()}')
            print(f'Path : {event.src_path}')
            print(f'Running {self.params.file}...')
            os.system(f'{self.command} {self.executable}')
            self.last_trigger = time.time()

    def should_trigger(self) -> bool:
        """Test whether it should trigger for the event.

        Returns:
            status (bool): True if it should trigger, False otherwise.
        """
        delta = time.time() - self.last_trigger
        return delta > self.params.time

    def get_command(self, test: bool) -> str:
        """Selects which command it should run.

        Args:
            test (bool): if it should run pytest.

        Return:
            command (str): which command it should run.
        """
        if test:
            return "pytest"
        return "python"

    def get_executable(self, directory: str, file_to_execute: str) -> str:
        """Builds string to execute.

        Args:
            dir (str): the directory it is looking
            file_to_execute (str): file that it should run.

        Returns:
            executable (str): complete command to execute.
        """
        executable = ""
        if directory is not None:
            executable += f"{directory}/"
        executable += file_to_execute
        return executable
