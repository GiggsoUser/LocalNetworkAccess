import pytest
from selenium import webdriver
import configparser
import os


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()  # Initialize Chrome WebDriver
    driver.implicitly_wait(10)  # Set implicit wait time
    yield driver
    driver.quit()


# second

# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome  import ChromeDriverManager
#
# @pytest.fixture(scope="session")
# def browser():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
