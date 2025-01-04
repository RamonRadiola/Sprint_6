import pytest
from selenium import webdriver
from pages.home_page import HomePage
from locators import Locators

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def home_page_start(driver):
    page = HomePage(driver)
    page.go_to_site(driver)
    page.click_button_cookie()
    page.scroll_to_element(Locators.QUESTION_0)
    return page

@pytest.fixture(scope="function")
def home_page_order(driver):
    page = HomePage(driver)
    page.go_to_site(driver)
    page.click_button_cookie()
    return page
