from argparse import ArgumentParser, Namespace


def get_args() -> Namespace:
    parser = ArgumentParser(description="Arguments for watching over a file")

    parser.add_argument(
        '-d',
        '--dir',
        type=str,
        default=None,
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

    params = parser.parse_args()
    params.dir = params.dir if params.dir != "None" else None

    return params
