from typing import Callable, List
from .parser import make_parser
from yaml import safe_load, YAMLError
from .dotdict import DotDict
import sys
from pathlib import Path

config_defaults = """
mockapi:
    host: localhost
    port: 8000

healthcheck:
    response:
        status: "OK"
"""

config = DotDict()


class OptionsError(Exception):
    ...


def yaml_loader(cfg_str):
    return safe_load(cfg_str)


def pre_main(
    app_name: str,
    app_version: str,
    args: List[str] = [],
    _make_parser: Callable = make_parser,
    cfg_default: dict = config_defaults,
):
    config.app = app_name
    config.version = app_version
    if cfg_default:
        cfg_default = yaml_loader(cfg_default)
        config.merge(cfg_default)

    if _make_parser:
        parser = _make_parser()
    else:
        parser = make_parser()

    cli = parser.parse_args(args)

    config.merge(cli)
    if config.mock_config:
        cli_config: Path = config.mock_config
        with cli_config.open("r") as cfg_file:
            try:
                cfg_f = safe_load(cfg_file.read())
            except YAMLError as exc:
                raise OptionsError("Error Loading Config Yaml") from exc
        config.merge(cfg_f)

    config.prefix = sys.prefix

    return config
