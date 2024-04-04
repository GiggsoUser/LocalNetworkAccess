import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def login(self):
        self.driver.find_element(By.XPATH, self.username_xpath).click()
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys("admin")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, self.password_xpath).click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys("02392")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

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
        try:
            menu_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.menu_xpath))
            )
            print("Page opened successfully.")
            # Additional actions if the menu item is found
            # For example, you can assert certain conditions to verify the correctness of the page
            assert "Expected Menu Item Text" in menu_element.text
        except:
            print("Page may not have loaded correctly or menu item not found.")
    def firmware_updates(self):
        self.driver.find_element(By.XPATH, self.updates_menu_xpath).click()
        self.driver.implicitly_wait(4)
