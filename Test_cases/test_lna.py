from Page_objects.base_class import Lna
import time
# from Page_objects.base_class1 import Lna
import logging
import pytest

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestLna:
    def test_login_page_loads_successfully(self):
        logger.info("Test started: Login page loads successfully")
        co = Lna()
        co.launch_browser_with_base_url()
        logger.info("Login page loaded successfully")
        co.driver.maximize_window()
        time.sleep(2)
        logger.info("Window maximized")
        co.proceed()
        logger.info("Security warning bypassed")
        co.login()
        logger.info("Login successful")
        time.sleep(5)
        co.update_pwd()
        logger.info("Password updated successfully")
        logger.info("Setup completed successfully")
        co.firmware_updates()
        logger.info("Navigated to firmware updates section")
        co.verify_menu()
        time.sleep(3)
#

# import logging
# import time
# import pytest
# from Page_objects.base_class import Lna
#
# # Set up logging
# logger = logging.getLogger(__name__)
#
# class TestLna:
#     def test_login_page_loads_successfully(self, browser):
#         logger.info("Test started: Login page loads successfully")
#         co = Lna(browser)
#         co.launch_browser_with_base_url()
#         logger.info("Login page loaded successfully")
#         co.driver.maximize_window()
#         time.sleep(2)
#         logger.info("Window maximized")
#         co.proceed()
#         logger.info("Security warning bypassed")
#         co.login()
#         logger.info("Login successful")
#         time.sleep(5)
#         co.update_pwd()
#         logger.info("Password updated successfully")
#         logger.info("Setup completed successfully")
#         co.firmware_updates()
#         logger.info("Navigated to firmware updates section")
#         co.verify_menu()
#         time.sleep(3)
