import allure

from locators import Locators

@allure.story("Тестируем выпадающий список раздела с вопросами и ответами")
class TestHomePage:
    @allure.step("Открываем первый вопрос")
    def test_question_0(self, home_page, driver):
        home_page.click_place_0()
        home_page.check_answer_0()
        assert 'Сутки — 400 рублей.' in driver.find_element(*Locators.ANSWER_0).text

    @allure.step("Открываем второй вопрос")
    def test_question_1(self, home_page, driver):
        home_page.click_place_1()
        home_page.check_answer_1()
        assert 'Пока что у нас так' in driver.find_element(*Locators.ANSWER_1).text

    @allure.step("Открываем третий вопрос")
    def test_question_2(self, home_page, driver):
        home_page.click_place_2()
        home_page.check_answer_2()
        assert 'вы оформляете заказ' in driver.find_element(*Locators.ANSWER_2).text

    @allure.step("Открываем четвертый вопрос")
    def test_question_3(self, home_page, driver):
        home_page.click_place_3()
        home_page.check_answer_3()
        assert 'начиная с завтрашнего дня' in driver.find_element(*Locators.ANSWER_3).text

    @allure.step("Открываем пятый вопрос")
    def test_question_4(self, home_page, driver):
        home_page.click_place_4()
        home_page.check_answer_4()
        assert 'Пока что нет' in driver.find_element(*Locators.ANSWER_4).text

    @allure.step("Открываем шестой вопрос")
    def test_question_5(self, home_page, driver):
        home_page.click_place_5()
        home_page.check_answer_5()
        assert 'Самокат приезжает к вам' in driver.find_element(*Locators.ANSWER_5).text

    @allure.step("Открываем седьмой вопрос")
    def test_question_6(self, home_page, driver):
        home_page.click_place_6()
        home_page.check_answer_6()
        assert 'пока самокат не привезли' in driver.find_element(*Locators.ANSWER_6).text