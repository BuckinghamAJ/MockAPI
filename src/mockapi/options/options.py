from typing import Callable, List
from .parser import make_parser
from yaml import safe_load
from .dotdict import DotDict
import sys

config_defaults = """
fast_api:
    host: localhost
    port: 8000

healthcheck:
    response:
        status: "OK"
"""

config = DotDict()


def yaml_loader(cfg_str):
    return safe_load(cfg_str)


def pre_main(
    app_name: str,
    app_version: str,
    args: List[str] = [],
    _make_parser: Callable = make_parser,
    cfg_default: dict = config_defaults,
):
    # TODO: Merge Config with Parser
    config.app = app_name
    config.version = app_version
    if cfg_default:
        cfg_default = yaml_loader(cfg_default)
        config.merge(cfg_default)

    # if args is None:
    # args = sys.argv

    if _make_parser:
        parser = _make_parser()
    else:
        parser = make_parser()

    cli = parser.parse_args(args)

    config.merge(cli)

    config.prefix = sys.prefix

    return config
