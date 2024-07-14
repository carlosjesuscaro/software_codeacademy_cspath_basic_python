import os
import logging
import logging.config
from datetime import datetime
from dotenv import find_dotenv, load_dotenv
from src.strings_basic import count_unique_letters

env_file = find_dotenv()
load_dotenv()

CONFIG_DIR = "./config"
LOG_DIR = "./logs"


def setup_logging():
    """Load logging configuration"""
    log_configs = {"dev": "logging.dev.ini", "prod": "logging.prod.ini"}
    config = log_configs.get(os.environ["ENV"])
    config_path = "/".join([CONFIG_DIR, config])

    # timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")
    timestamp = datetime.now().strftime("%Y%m%d")

    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults={"logfilename": f"{LOG_DIR}/{os.environ['ENV']}.{timestamp}.log"},
    )

def string_challenge() -> None:
    """Runs all the exercises defined in the string challenge
    Args: None
    Returns: None
    Raises: None
    """
    count_unique_letters('carlos')
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Program started")
    string_challenge()
    logger.info("Program finished")
