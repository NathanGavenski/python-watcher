from argparse import Namespace
import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent

from arguments import get_args


# TODO event from VS Code and vim are different, one picks up the path the other no
class EventHandler(FileSystemEventHandler):
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
        delta = time.time() - self.last_trigger
        if 'swp' not in event.src_path and delta > self.params.time:
            os.system('clear')
            print(f'Event type: {str(event.event_type).upper()}')
            print(f'Path : {event.src_path}')
            print(f'Running {self.params.file}...')
            os.system(f'{self.command} {self.executable}')
            self.last_trigger = time.time()

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

    def get_executable(self, dir: str, file_to_execute: str) -> str:
        """Builds string to execute.

        Args:
            dir (str): the directory it is looking
            file_to_execute (str): file that it should run.

        Returns:
            executable (str): complete command to execute.
        """
        executable = ""
        if dir is not None:
            executable += f"{dir}/"
        executable += file_to_execute
        return executable


def setup_observer(params: Namespace, handler: EventHandler) -> Observer:
    """Creates observer.

    Args:
        params (Namespace): arguments from command line.
        handler (EventHandler): custom handler to handle events

    Returns:
        observer (Observer): observer to execute watcher and trigger events.
    """
    observer = Observer()
    directory = params.dir if params.dir is not None else params.file
    observer.schedule(handler, path=directory, recursive=True)
    return observer


def main() -> None:
    """Execute watcher (for command line)."""
    params = get_args()

    os.system('clear')
    if params.dir is not None:
        print(f'Watching: {params.dir}')
    print(f'Executing: {params.file}')

    event_handler = EventHandler(params)
    observer = setup_observer(params, event_handler)
    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.join()


if __name__ == "__main__":
    main()
