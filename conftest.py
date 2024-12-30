import pytest
from selenium import webdriver
from pages.home_page import HomePage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def home_page(driver):
    page = HomePage(driver)
    page.go_to_site(driver)
    page.scroll_to_element(driver)
    return page
