"""Abstract Base Class for the different endpoint controllers. """
from mockapi.options.dotdict import DotDict
from abc import abstractmethod, ABC
from pathlib import Path


class AbstractMockController(ABC):
    def __init__(self, file: Path, cfg: DotDict) -> None:
        self.file = file
        self.cfg = cfg

    @property
    @abstractmethod
    def responses(self):
        raise NotImplemented

    @property
    @abstractmethod
    def end_point(self):
        raise NotImplemented

    @abstractmethod
    async def parse_file(self):
        raise NotImplemented


class MockController(AbstractMockController):
    @property
    def end_point(self):
        return self.file.stem
