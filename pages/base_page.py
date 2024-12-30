from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    def go_to_site(self, driver):
        self.driver.get(self.url)
        return WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SIGNAL_LOGO_SCOOTER))

    def find_element_for_click(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not find element {locator}')

    def find_element_for_visio(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not find element {locator}')