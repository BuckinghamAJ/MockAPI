from argparse import ArgumentParser
import sys
from pathlib import Path

base_dir = sys.prefix


def make_parser():
    parser = ArgumentParser()

    parser.add_argument(
        "-f",
        "--response-file",
        dest="response",
        default=Path(base_dir, "config", "response.yml"),
        required=False,
        help="Define mocker's responses with yaml file",
    )

    return parser
