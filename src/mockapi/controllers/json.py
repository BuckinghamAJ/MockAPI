from .base import MockController


class JsonController(MockController):
    @property
    def responses(self):
        return {"Hello": "World"}

    async def parse_file(self):
        ...
