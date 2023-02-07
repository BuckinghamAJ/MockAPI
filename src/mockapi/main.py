from fastapi import FastAPI
from mockapi import name, version, description
from mockapi.options import pre_main
from mockapi.log import configure_logger
from gunicorn.app.base import BaseApplication
from mockapi.controllers.manager import ResponseManager
from uvicorn import run
import sys
import logging

app = FastAPI(title=name, description=description, version=version)
log = logging.getLogger(__name__)


class StandaloneApplication(BaseApplication):
    """Our Gunicorn application."""

    def __init__(self, app, options=None):
        self.options = options or {}
        self.mgr = ResponseManager(cfg=options)
        self.application = app
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def fast_run():

    config = pre_main(app_name=name, app_version=version, args=sys.argv[1:])
    log_options = configure_logger(config)

    config.merge(log_options)
    StandaloneApplication(app, config).run()


if __name__ == "__main__":
    fast_run()
