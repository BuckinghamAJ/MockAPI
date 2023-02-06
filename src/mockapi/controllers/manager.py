import asyncio
from pathlib import Path
import mockapi
import logging
from mockapi.error import MockerException

log = logging.getLogger(__name__)

NotFound = object()


class ResponseManager:

    _mock_files = NotFound

    def __init__(self, cfg):
        self.cfg = cfg
        self.create_responses()

    @property
    def mock_files(self):
        cfg = self.cfg
        _mock_files = self._mock_files
        if _mock_files is NotFound:
            if cfg.directory:
                log.debug("Directory -> %r" % (cfg.directory))
                _mock_files = [
                    rsp_path
                    for rsp_path in Path(cfg.directory).glob("*")
                    if str(rsp_path.name).startswith("mock_")
                ]
            elif cfg.response_file:
                _mock_files = [Path(cfg.response_file)]
            else:
                _mock_files = [
                    rsp_path
                    for rsp_path in Path(mockapi.__path__[0], "responses").glob("*")
                    if str(rsp_path.name).startswith("mock_")
                ]
        return _mock_files

    def create_responses(self):
        # Defaults looking in the responses path
        log.debug("Mock Files Found -> %r" % (self.mock_files))
        for mock_file in self.mock_files:
            if mock_file.endswith(".json"):
                ...
            elif mock_file.endswith(".yml") or mock_file.endswith(".yaml"):
                ...
            else:
                raise MockerException("Invalid response file type")
