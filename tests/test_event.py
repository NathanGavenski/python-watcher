from argparse import Namespace
from typing import Any, List
from unittest import TestCase, mock


from src.watcher.event import EventHandler


class TestWatcher(TestCase):
    """Test cases for watcher file"""

    def test_eventhandler_command(self) -> None:
        event = EventHandler(Namespace(dir=None, file="test.py", test=False))
        assert event.command == "python"

        event = EventHandler(Namespace(dir=None, file="test.py", test=True))
        assert event.command == "pytest"

    def test_eventhandler_executable(self) -> None:
        event = EventHandler(Namespace(dir=None, file="test.py", test=False))
        assert event.executable == "test.py"

        event = EventHandler(Namespace(dir=".", file="test.py", test=False))
        assert event.executable == "./test.py"

    def test_eventhandler_should_trigger(self) -> None:
        event = EventHandler(Namespace(dir=".", file="test.py", test=False, time=0))
        assert event.should_trigger()

        event = EventHandler(Namespace(dir=".", file="test.py", test=False, time=1))
        assert not event.should_trigger()
