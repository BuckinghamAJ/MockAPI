from .base import MockController


class YamlController(MockController):
    @property
    def responses(self):
        return {"Hello": "World"}

    async def parse_file(self):
        ...
