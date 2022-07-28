import logging
import os

from config import Config


def create_logger(cfg: Config) -> logging.Logger:
    logger = logging.getLogger(cfg.LOGGER_NAME)
    logger.setLevel(cfg.LOG_LEVEL)

    if not os.path.exists(cfg.LOG_DIR):
        os.makedirs(cfg.LOG_DIR)

    fh = logging.FileHandler(f"{cfg.LOG_DIR}/all.log")
    fh.setLevel(cfg.LOG_LEVEL)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger