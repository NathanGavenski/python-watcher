"""Module for arguments when calling watcher."""
from argparse import ArgumentParser, Namespace


def get_args() -> Namespace:
    """Function for getting command line arguments."""
    parser = ArgumentParser(description="Arguments for watching over a file")

    parser.add_argument(
        '-d',
        '--dir',
        type=str,
        default='.',
        help='Directory to observe'
    )
    parser.add_argument(
        '-f',
        '--file',
        type=str,
        help='File name to execute when observes a new change'
    )
    parser.add_argument(
        '-t',
        '--time',
        type=int,
        default=1,
        help='Time delay to run again (good when saving constantly)'
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help='whether watcher should run pytest'
    )
    parser.add_argument(
        '--lint',
        action='store_true',
        help='whether watcher should run pylint'
    )
    parser.add_argument(
        '--lint_src',
        type=str,
        default='src',
        help='where to run pylint'
    )

    params = parser.parse_args()
    params.dir = params.dir if params.dir != "None" else None

    return params
