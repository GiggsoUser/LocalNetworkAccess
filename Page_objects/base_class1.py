import webbrowser
import time
import psutil
import logging

from selenium.webdriver.common.by import By

# Configure logging
logging.basicConfig(filename='browser_launch.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


def launch_chrome(url):
    logging.info("Launching Chrome browser.")
    # Specify the URL you want to open
    webbrowser.open(url, new=2)


def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False


def verify_browser_launch():
    # Wait for a while to allow the browser to open
    time.sleep(5)  # Adjust this time as needed
    if is_process_running("chrome.exe"):
        logging.info("Chrome browser is running. Browser launched successfully.")
        return True
    else:
        logging.error("Chrome browser is not running. Browser launch failed.")
        return False


# Function to simulate login
def simulate_login(self):
    logging.info("Simulating login...")
    self.driver.find_element(By.XPATH, self.advanced_button_xpath).click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, self.proceed_xpath).click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, self.username_xpath).click()
    self.driver.find_element(By.XPATH, self.username_xpath).send_keys("admin")
    self.driver.find_element(By.XPATH, self.password_xpath).click()
    self.driver.find_element(By.XPATH, self.password_xpath).send_keys("02392")
    self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    # Insert login code here
    # Replace the following line with actual login verification logic
    return True  # Placeholder for successful login


# Function to simulate menu navigation
def simulate_menu_navigation():
    logging.info("Simulating menu navigation...")
    # Insert menu navigation code here
    # Replace the following line with actual menu navigation verification logic
    return True  # Placeholder for successful navigation


# Function to simulate URL launch
def simulate_url_launch(url):
    logging.info(f"Simulating launch of URL: {url}")
    # Insert URL launch code here
    # Replace the following line with actual URL launch verification logic
    return True  # Placeholder for successful URL launch


# Example URL to open in Chrome
# url = "https://www.giggso.com"
url = "https://192.168.1.80"

# Call the function to launch Chrome with the specified URL
launch_chrome(url)

# Verify browser launch
assert verify_browser_launch(), "Failed to launch Chrome browser."

# Verify login
assert simulate_login(), "Login failed."

# Verify menu navigation
assert simulate_menu_navigation(), "Menu navigation failed."

# Verify URL launch
assert simulate_url_launch(url), f"Failed to launch URL: {url}"

print("All steps executed successfully.")
