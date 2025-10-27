import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

class DriverSetup:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.base_url = "file://" + os.path.abspath("index.html")

    def setup_driver(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-plugins")
            chrome_options.add_argument("--disable-images")

            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.implicitly_wait(10)
            self.wait = WebDriverWait(self.driver, 15)
            print("Chrome WebDriver initialized")
            return self.driver
        except WebDriverException as e:
            print(f"Error initializing WebDriver: {e}")
            raise

    def navigate_to_homepage(self):
        try:
            print(f"Navigating to: {self.base_url}")
            self.driver.get(self.base_url)
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-grid")))
            title = self.driver.title
            assert "Mini E-Kart" in title, f"Expected 'Mini E-Kart' in title, got {title}"
            print("Opened Mini E-Kart homepage")
            return True
        except TimeoutException:
            print("Timeout waiting for page to load")
            return False
        except Exception as e:
            print(f"Error navigating to homepage: {e}")
            return False

    def find_element_safely(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"Element not found: {by}={value}")
            return None

    def find_elements_safely(self, by, value, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
            return elements
        except TimeoutException:
            print(f"Elements not found: {by}={value}")
            return []

    def click_element_safely(self, element, desc="element"):
        try:
            if element and element.is_displayed() and element.is_enabled():
                element.click()
                print(f"Clicked {desc}")
                time.sleep(0.5)
                return True
            else:
                print(f"{desc} not clickable")
                return False
        except Exception as e:
            print(f"Error clicking {desc}: {e}")
            return False

    def get_text_safely(self, element, desc="element"):
        try:
            if element:
                text = element.text.strip()
                return text
            else:
                print(f"{desc} not found for text")
                return ""
        except Exception as e:
            print(f"Error getting text from {desc}: {e}")
            return ""

    def take_screenshot(self, filename="screenshot.png"):
        try:
            path = os.path.join("reports", filename)
            self.driver.save_screenshot(path)
            print(f"Screenshot saved: {path}")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")

    def cleanup(self):
        try:
            if self.driver:
                self.driver.quit()
                print("WebDriver closed")
        except Exception as e:
            print(f"Error closing WebDriver: {e}")

    def get_driver(self):
        return self.driver

    def get_wait(self):
        return self.wait


driver_setup = DriverSetup()

def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
    context.driver_setup = DriverSetup()
    context.driver = context.driver_setup.setup_driver()
    context.wait = context.driver_setup.get_wait()
    ok = context.driver_setup.navigate_to_homepage()
    if not ok:
        raise Exception("Could not open homepage")

def after_scenario(context, scenario):
    print(f"Completed scenario: {scenario.name}")
    if hasattr(context, 'driver_setup'):
        context.driver_setup.cleanup()
    print("-" * 40)