# source/base_page.py
import inspect
import logging
import os
from datetime import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
log_handler=False

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @staticmethod
    def get_logger():
        global log_handler
        # Get the caller function name (used as logger name)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # Avoid adding multiple handlers
        if logger.handlers:
            return logger

        # Ensure logs/ directory exists
        os.makedirs("logs", exist_ok=True)

        # Detect if we're running in parallel (pytest-xdist)
        worker_id = os.environ.get('PYTEST_XDIST_WORKER')
        # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if worker_id:
            # Parallel execution: unique log file per worker
            log_file = os.path.join("logs", f"{logger_name}_{worker_id}.log")
        else:
            # Normal execution: one common log file
            log_file = os.path.join("logs", "logfile.log")

        # Set up file handler
        if not log_handler:
            file_handler = logging.FileHandler(log_file, mode='w')
            log_handler=True
        else:
            file_handler = logging.FileHandler(log_file, mode='a')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(filename)s: %(funcName)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)

        return logger
