import asyncio
import aiofiles
from pathlib import Path
import mockapi

NotFound = object()


class ResponseManager:

    _mock_files = NotFound

    def __init__(self, cfg):
        asyncio.run(self.async_initialization(cfg))

    @property
    def mock_files(self):
        cfg = self.cfg
        _mock_files = self._mock_files
        if _mock_files is NotFound:
            if cfg.directory:
                # TODO: Add parser option if just using as command line tool
                ...
            else:
                _mock_files = [
                    rsp_path
                    for rsp_path in Path(mockapi.__path__[0], "responses")
                    if rsp_path.startswith("mock_")
                ]
        return _mock_files

    async def async_initialization(self):
        # Defaults looking in the responses path
        mock_files = None
