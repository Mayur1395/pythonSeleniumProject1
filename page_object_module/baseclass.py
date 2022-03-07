import logging

import pytest


@pytest.mark.usefixtures("test_setup")
class Baseclass:
    def test_logging(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler("loging.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)
        logger.debug("debug statement executed")
        logger.info("information statement")
        logger.warning("something is warning in mode")
        logger.error("error is found")
        logger.critical("critical issue")
        return logger



