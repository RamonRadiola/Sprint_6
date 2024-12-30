from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators import Locators
from constants import Constants
import allure

@allure.story("Тестируем позитивный сценарий заказа")
class TestOrderPage:
    @allure.step("Первый сценарий через кнопку сверху")
    def test_positive_order_first(self, driver):
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        home_page.go_to_site(driver)
        home_page.click_button_order(locator=Locators.BUTTON_ORDER_UP)
        order_page.input_name(name="Лиля")
        order_page.input_surname(surname="Брикс")
        order_page.input_addres(addres="Москва, Покровскакая 4")
        order_page.input_number(number="89001001020")
        order_page.click_metro_holder()
        order_page.choose_station(locator=Locators.PHOLD_ClEAN_PONDS)
        order_page.button_next()
        order_page.click_element_order(locator=Locators.PHOLD_DATA_CHOOSE_1)
        order_page.click_rental_period(locator=Locators.RENTAL_1_DAYS)
        order_page.choose_color()
        order_page.comment_for_courier(comment="Я вас очень жду")
        order_page.click_button_order_down()
        order_page.click_button_yes()
        order_page.check_button_status()
        assert 'Заказ оформлен' in driver.find_element(*Locators.SIGNAL_ORDER_IS_READY_2).text

    @allure.step("Второй сценарий через кнопку снизу")
    def test_positive_order_second(self, driver):
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        home_page.go_to_site(driver)
        home_page.click_button_order(locator=Locators.BUTTON_ORDER_DOWN)
        order_page.input_name(name="Маша")
        order_page.input_surname(surname="Фридман")
        order_page.input_addres(addres="Москва, Литий-йонная 13")
        order_page.input_number(number="89505456045")
        order_page.click_metro_holder()
        order_page.choose_station(locator=Locators.PHOLD_ClEAN_PONDS)
        order_page.button_next()
        order_page.click_element_order(locator=Locators.PHOLD_DATA_CHOOSE_2)
        order_page.click_rental_period(locator=Locators.RENTAL_5_DAYS)
        order_page.choose_color()
        order_page.comment_for_courier(comment="Мороженое оставьте себе!")
        order_page.click_button_order_down()
        order_page.click_button_yes()
        order_page.check_button_status()
        assert 'Заказ оформлен' in driver.find_element(*Locators.SIGNAL_ORDER_IS_READY_2).text

    @allure.step("Переход по логотипу 'самокат'")
    def test_click_scooter(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site(driver)
        home_page.click_button_order(locator=Locators.BUTTON_ORDER_UP)
        home_page.click_logo_scooter()
        assert driver.current_url == Constants.URL

    @allure.step("Переход по логотипу 'Яндекс'")
    def test_click_ya(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site(driver)
        original_window = driver.current_window_handle
        home_page.click_logo_ya()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        windows = driver.window_handles
        for window in windows:
            if window != original_window:
                driver.switch_to.window(window)
                break
        expected_url = Constants.URL_DZEN
        try:
            WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        except Exception as e:
            print(f"Ошибка при ожидании URL: {e}")
        assert driver.current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {driver.current_url}"