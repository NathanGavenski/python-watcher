"""Module for testing watcher functions."""
from argparse import Namespace
from typing import Any, List
from unittest import TestCase, mock

from watchdog.observers import Observer

from src.watcher.event import EventHandler
from src.watcher.watcher import setup_observer


class TestWatcher(TestCase):
    """Test cases for watcher file"""

    @mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=Namespace(dir=None, file="test.py", test=False)
    )
    def setUp(self, params: Namespace) -> None:
        """Setup function for all tests."""
        self.params = params

    def get_handlers(self, observer: Observer) -> List[Any]:
        """Get handlers from observer."""
        return list(list(observer._handlers.values())[0])

    def get_watches(self, observer) -> Any:
        """Get watchers from observer."""
        return observer._watches.pop()

    def test_setup_observer(self) -> None:
        """Test setup of the observer."""
        event = EventHandler(self.params)
        observer = setup_observer(self.params, event)

        assert not observer.is_alive()
        assert isinstance(self.get_handlers(observer)[0], EventHandler)
        assert self.get_watches(observer).is_recursive
