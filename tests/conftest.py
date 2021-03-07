import logging


from utils import log as log_utils

LOG_LEVEL = logging.DEBUG

TEST_LOGGER_NAME = "test-logger"

TEST_LOGGER = log_utils.get_logger(name=TEST_LOGGER_NAME, handlers=[log_utils.get_stream_handler(level=LOG_LEVEL)], level=LOG_LEVEL)
