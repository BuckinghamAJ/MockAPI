import asyncio
from pathlib import Path
from typing import Dict
import mockapi
import logging
from mockapi.error import MockerException
from .base import MockController
from .json import JsonController
from .yaml import YamlController

log = logging.getLogger(__name__)

NotFound = object()


class ResponseManager:

    _mock_files = NotFound

    def __init__(self, cfg):
        self.cfg = cfg
        self.responses: dict[str, MockController] = None
        self.create_responses()

    @property
    def mock_files(self) -> list[Path]:
        cfg = self.cfg
        _mock_files = self._mock_files
        if _mock_files is NotFound:
            if cfg.directory:
                log.debug(
                    "🐍 File: controllers/manager.py | Line: 26 | mock_files ~ cfg.directory = %r"
                    % (cfg.directory,)
                )
                _mock_files = [
                    rsp_path
                    for rsp_path in Path(cfg.directory).glob("*")
                    if rsp_path.name.startswith("mock_")
                ]
            elif cfg.response_file:
                log.debug(
                    "🐍 File: controllers/manager.py | Line: 36 | mock_files ~ cfg.response_file = %r"
                    % (cfg.response_file)
                )
                _mock_files = [cfg.response_file]
            else:
                _mock_files = [
                    rsp_path
                    for rsp_path in Path(mockapi.__path__[0], "responses").glob("*")
                    if rsp_path.name.startswith("mock_")
                ]
            if not _mock_files:
                raise MockerException("No mock files provided")
        return _mock_files

    def create_responses(self) -> None:
        # Defaults looking in the responses path
        log.debug(
            "🐍 File: controllers/manager.py | Line: 45 | create_responses ~ self.mock_files = %r"
            % (self.mock_files,)
        )
        responses = {}
        for mock_file in self.mock_files:
            if mock_file.suffix == ".json":
                responses[mock_file.stem] = JsonController(mock_file, self.cfg)
            elif mock_file.suffix in (".yml", ".yaml"):
                responses[mock_file.stem] = YamlController(mock_file, self.cfg)
            else:
                raise MockerException("Invalid response file type")

        self.responses = responses

    def find_response_by(self, name: str):
        return self.responses.get(name)
