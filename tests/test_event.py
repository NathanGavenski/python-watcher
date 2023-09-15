"""Module for testing EventHandler class"""
from argparse import Namespace
from copy import deepcopy
from unittest import TestCase

from src.watcher.event import EventHandler


class TestWatcher(TestCase):
    """Test cases for watcher file"""

    def setUp(self) -> None:
        """Setup cli parameters."""
        self.params = Namespace(
            dir=None,
            file="test.py",
            test=False,
            lint=False,
            lint_src="src",
            time=1
        )

    def get_params(self) -> Namespace:
        """Get a deepcopy from cli parameters."""
        return deepcopy(self.params)

    def test_eventhandler_command(self) -> None:
        """Test cp,,amd that has to run."""
        event = EventHandler(self.get_params())
        assert event.command == "python"

        params = self.get_params()
        params.test = True
        event = EventHandler(params)
        assert event.command == "pytest"

        params = self.get_params()
        params.lint = True
        event = EventHandler(params)
        assert event.command == "pylint"

    def test_eventhandler_executable(self) -> None:
        """Test command that is executed."""
        event = EventHandler(self.get_params())
        assert event.executable == "test.py"

        params = self.get_params()
        params.dir = "."
        event = EventHandler(params)
        assert event.executable == "./test.py"

        params = self.get_params()
        params.lint = True
        event = EventHandler(params)
        assert event.executable == "src"

    def test_eventhandler_should_trigger(self) -> None:
        """Test if it should trigget event."""
        params = self.get_params()
        params.time = 0
        event = EventHandler(params)
        assert event.should_trigger()

        event = EventHandler(self.get_params())
        assert not event.should_trigger()
