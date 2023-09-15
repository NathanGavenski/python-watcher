"""Setup a path to the maze folder."""
import sys
import pathlib

PACKAGE_PARENT = pathlib.Path(__file__).parent
SCRIPT_DIR = PACKAGE_PARENT / "src"
sys.path.append(str(SCRIPT_DIR))
