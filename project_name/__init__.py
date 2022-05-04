import os
from datetime import datetime
from photonai.photonlogger import logger

current_path = os.path.dirname(os.path.abspath(__file__))
registered_file = os.path.join(current_path, "registered")
logger.info("Checking project_name Module Registration")
if not os.path.isfile(registered_file):  # pragma: no cover
    logger.info("Registering project_name")
    from photonai.base import PhotonRegistry
    reg = PhotonRegistry()
    reg.add_module(os.path.join(current_path, "project_name.json"))
    with open(os.path.join(registered_file), "w") as f:
        f.write(str(datetime.now()))
