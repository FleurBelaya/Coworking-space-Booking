import logging
import os
import sys
from pathlib import Path

from loguru import logger

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)


class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger.opt(depth=6, exception=record.exc_info).log(
            record.levelname, record.getMessage()
        )


def setup_logging():
    env = os.getenv("APP_ENV", "dev")
    level = os.getenv("LOG_LEVEL", "INFO")

    logger.remove()

    if env == "prod":
        logger.add(
            sys.stdout,
            level=level,
            serialize=True,
            enqueue=True,
        )
    else:
        fmt = (
            "<green>{time:HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        )
        logger.add(sys.stdout, level=level, format=fmt)

    logger.add(
        LOG_DIR / "app.log",
        rotation="10 MB",
        retention="7 days",
        compression="zip",
        level=level,
        serialize=(env == "prod"),
    )

    logging.basicConfig(
        handlers=[InterceptHandler()],
        level=0,
        force=True,
    )

    return logger
