from fastapi import FastAPI
from mockapi import name, version, description
from mockapi.options import pre_main
from uvicorn import run
import logging

log = logging.getLogger()

app = FastAPI(title=name, description=description, version=version)


def fast_run():
    cfg = pre_main(app_name=name, app_version=version)
    fast_cfg = cfg.fast_api
    run(app=app, host=fast_cfg.host, port=fast_cfg.port)


if __name__ == "__main__":
    fast_run()
