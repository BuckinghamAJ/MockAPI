from argparse import ArgumentParser
import sys
from pathlib import Path

base_dir = sys.prefix


def make_parser():
    parser = ArgumentParser()

    parser.add_argument(
        "-c",
        "--config",
        dest="mock_config",
        default=Path(base_dir, "config", "config.yml"),
        required=False,
        help="Define mocker's responses with yaml file",
    )

    parser.add_argument(
        "-f",
        "--response-file",
        dest="response_file",
        required=False,
        help="Define mocker's responses with yaml file",
    )
    parser.add_argument(
        "-d",
        "--directory",
        dest="directory",
        default=Path(base_dir, "responses"),
        required=False,
        help="Pass in directory with response files",
    )

    return parser
