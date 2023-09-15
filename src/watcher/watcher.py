"""File for watcher specific functions."""
from argparse import Namespace
import os

from watchdog.observers import Observer

from watcher.arguments import get_args
from watcher.event import EventHandler


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
    print(f'Executing: {params.file if not params.test else "pytest"}')

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
