"""Abstract Base Class for the different endpoint controllers. """
from mockapi.options.dotdict import DotDict
from abc import abstractmethod, ABC


class MockController(ABC):
    def __init__(self, cfg: DotDict) -> None:
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
    async def parse_file(self, file):
        raise NotImplemented
