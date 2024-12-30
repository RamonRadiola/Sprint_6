from pages.base_page import BasePage
from locators import Locators


class OrderPage(BasePage):
    def check_visio_test(self):
        self.find_element_for_visio(locator=Locators.SIGNAL_ORDER_1)

    def input_name(self, name):
        self.find_element_for_visio(locator=Locators.PHOLD_NAME).send_keys(name)

    def input_surname(self, surname):
        self.find_element_for_visio(locator=Locators.PHOLD_SURNAME).send_keys(surname)

    def input_addres(self, addres):
        self.find_element_for_visio(locator=Locators.PHOLD_ADDRES).send_keys(addres)

    def click_metro_holder(self):
        self.find_element_for_click(locator=Locators.PHOLD_METRO).click()

    def choose_station(self, locator):
        self.find_element_for_click(locator).click()

    def input_number(self, number):
        self.find_element_for_visio(locator=Locators.PHOLD_NUMBER).send_keys(number)

    def button_next(self):
        self.find_element_for_click(locator=Locators.BUTTON_NEXT).click()

    def click_element_order(self, locator):
        self.find_element_for_click(locator=Locators.PHOLD_DATA).click()
        self.find_element_for_click(locator).click()

    def click_rental_period(self, locator):
        self.find_element_for_click(locator=Locators.RENTAL_PERIOD).click()
        self.find_element_for_click(locator).click()

    def choose_color(self):
        self.find_element_for_click(locator=Locators.POINT_BLACK).click()

    def comment_for_courier(self, comment):
        self.find_element_for_click(locator=Locators.PHOLD_COMMENT).send_keys(comment)

    def click_button_order_down(self):
        self.find_element_for_click(locator=Locators.BUTTON_ORDER_DOWN_2).click()

    def click_button_yes(self):
        self.find_element_for_click(locator=Locators.BUTTON_YES).click()

    def check_button_status(self):
        self.find_element_for_click(locator=Locators.BUTTON_SEE_STATUS)

    def order_is_ready(self):
        self.find_element_for_visio(locator=Locators.SIGNAL_ORDER_IS_READY)