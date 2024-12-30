from pages.base_page import BasePage
from locators import Locators


class HomePage(BasePage):
    def scroll_to_element(self, driver):
        element = driver.find_element(*Locators.QUESTION_0)
        driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_place_0(self):
        self.find_element_for_click(locator=Locators.QUESTION_0).click()

    def check_answer_0(self):
        self.find_element_for_visio(locator=Locators.ANSWER_0)

    def click_place_1(self):
        self.find_element_for_click(locator=Locators.QUESTION_1).click()

    def check_answer_1(self):
        self.find_element_for_visio(locator=Locators.ANSWER_1)

    def click_place_2(self):
        self.find_element_for_click(locator=Locators.QUESTION_2).click()

    def check_answer_2(self):
        self.find_element_for_visio(locator=Locators.ANSWER_2)

    def click_place_3(self):
        self.find_element_for_click(locator=Locators.QUESTION_3).click()

    def check_answer_3(self):
        self.find_element_for_visio(locator=Locators.ANSWER_3)

    def click_place_4(self):
        self.find_element_for_click(locator=Locators.QUESTION_4).click()

    def check_answer_4(self):
        self.find_element_for_visio(locator=Locators.ANSWER_4)

    def click_place_5(self):
        self.find_element_for_click(locator=Locators.QUESTION_5).click()

    def check_answer_5(self):
        self.find_element_for_visio(locator=Locators.ANSWER_5)

    def click_place_6(self):
        self.find_element_for_click(locator=Locators.QUESTION_6).click()

    def check_answer_6(self):
        self.find_element_for_visio(locator=Locators.ANSWER_6)

    #метод клика по кнопке заказа сверху на главной
    def click_button_order(self, locator):
        self.find_element_for_visio(locator=Locators.BUTTON_ORDER_UP).click()

    def click_button_cookie(self):
        self.find_element_for_click(locator=Locators.BUTTON_COOKIE).click()

    def click_logo_scooter(self):
        self.find_element_for_click(locator=Locators.LOGO_WORD_SCOOTER).click()

    def click_logo_ya(self):
        self.find_element_for_click(locator=Locators.LOGO_WORD_YANDEX).click()










