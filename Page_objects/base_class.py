import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Lna:
    base_url = "https://192.168.1.80"
    username = "admin"
    password = "02392"
    username_xpath = "//*[@id='username']"
    password_xpath = "//*[@id='password']"
    new_password_xpath = "//*[@id='password']"
    confirm_password_xpath = "(//*[@type='password'])[2]"
    confirm_pwd_xpath = "/html/body/div/div[1]/div[1]/div/div/form/div[8]/input"
    submit_xpath = "//*[@id='app']/div[1]/div[1]/div/div/form/button"
    submit_button_xpath = "//*[@type='submit']"
    enter_new_xpath = "//*[@id='username']"
    confirm_pwd_xpath = "//*[@id='username']"
    updates_menu_xpath = "//*[@id='app']/main/div[1]/div[1]/div[1]/div[2]/div/a[3]/div[2]"
    advanced_button_xpath = "//*[@id='details-button']"
    proceed_xpath = "//*[@id='proceed-link']"
    context_xpath = "//*[@id='app']/main/div[1]/div[2]/div/div/div/div"
    menu_xpath = "//*[@id='app']/main/div[1]/div[2]/div/div/div[1]/button"
    login_button_xpath = "//*[@id='app']/div[1]/div[1]/div/div/form/button"

    def __init__(self):
        self.driver = None

    def launch_browser_with_base_url(self):
        self.driver = webdriver.Chrome()  # Initialize Chrome WebDriver
        self.driver.implicitly_wait(10)  # Set implicit wait time
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(5)
    def proceed(self):
        self.driver.find_element(By.XPATH, self.advanced_button_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.proceed_xpath).click()
        self.driver.implicitly_wait(5)

    def verify_login_page_loads(self):
        current_url = self.driver.current_url
        print("Current URL:", current_url)
        if 'login' in current_url:
            print("Login page is loaded")
        else:
            print("Login page is not loaded")
    def login(self):
        self.driver.find_element(By.XPATH, self.username_xpath).click()
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys("admin")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, self.password_xpath).click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys("02392")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def verify_update_pwd(self):
        current_url = self.driver.current_url
        print("Current URL:", current_url)
        if 'passwordChange' in current_url:
            print("passwordChange page is loaded")
        else:
            print("passwordChange page is not loaded")

    def update_pwd(self):
        self.driver.find_element(By.XPATH, self.new_password_xpath).click()
        self.driver.find_element(By.XPATH, self.new_password_xpath).send_keys("Network@123")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.new_password_xpath).send_keys(Keys.TAB)
        # self.driver.find_element(By.XPATH, self.confirm_pwd_xpath).click()
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys("Network@123")
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()
        self.driver.find_element(By.XPATH, self.username_xpath).click()
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys("admin")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, self.password_xpath).click()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys("Network@123")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()
        self.driver.implicitly_wait(2)

    def verify_menu(self):
        current_url = self.driver.current_url
        print("Current URL:", current_url)
        if 'update' in current_url:
            print("update menu is loaded")
        else:
            print("update menu is not loaded")


    def firmware_updates(self):
        self.driver.find_element(By.XPATH, self.updates_menu_xpath).click()
        self.driver.implicitly_wait(4)
