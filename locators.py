from selenium.webdriver.common.by import By


class Locators:
    QUESTION_0 = (By.ID, 'accordion__heading-0')
    ANSWER_0 = (By.XPATH, '//*[@id="accordion__panel-0"]/p')

    QUESTION_1 = (By.ID, 'accordion__heading-1')
    ANSWER_1 = (By.XPATH, '//*[@id="accordion__panel-1"]/p')

    QUESTION_2 = (By.ID, 'accordion__heading-2')
    ANSWER_2 = (By.XPATH, '//*[@id="accordion__panel-2"]/p')

    QUESTION_3 = (By.ID, 'accordion__heading-3')
    ANSWER_3 = (By.XPATH, '//*[@id="accordion__panel-3"]/p')

    QUESTION_4 = (By.ID, 'accordion__heading-4')
    ANSWER_4 = (By.XPATH, '//*[@id="accordion__panel-4"]/p')

    QUESTION_5 = (By.ID, 'accordion__heading-5')
    ANSWER_5 = (By.XPATH, '//*[@id="accordion__panel-5"]/p')

    QUESTION_6 = (By.ID, 'accordion__heading-6')
    ANSWER_6 = (By.XPATH, '//*[@id="accordion__panel-6"]/p')

    QUESTION_7 = (By.ID, 'accordion__heading-7')
    ANSWER_7 = (By.XPATH, '//*[@id="accordion__panel-7"]/p')

    SIGNAL_LOGO_SCOOTER = (By.XPATH, '//*/div[2]/div[1]/img') #ссылка логотипа скутера на главной
    SIGNAL_ORDER_1 = (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]') #надпись "Для кого самокат"
    SIGNAL_FORM = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    SIGNAL_FORM_2 = (By.CLASS_NAME, "Order_Header__BZXOb") #Надпись "про аренду"
    LOGO_WORD_YANDEX = (By.XPATH, '//*[@alt = "Yandex"]')  # логотип ЯНДЕКС на главной
    LOGO_WORD_SCOOTER = (By.XPATH, '//*[@alt = "Scooter"]')  # логотип САМОКАТ на главной
    LOGO_DZEN = (By.CLASS_NAME, "arrow__input mini-suggest__input")

    PHOLD_NAME = (By.XPATH, '//*[@placeholder="* Имя"]')
    PHOLD_SURNAME = (By.XPATH, '//*[@placeholder="* Фамилия"]')
    PHOLD_ADDRES = (By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]')
    PHOLD_NUMBER = (By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]')
    PHOLD_METRO = (By.XPATH, '//*[@placeholder="* Станция метро"]')
    PHOLD_ClEAN_PONDS = (By.CLASS_NAME, "Order_SelectOption__82bhS")
    PHOLD_DATA = (By.XPATH, '//*[@placeholder="* Когда привезти самокат"]') #дата доставки

    PHOLD_DATA_CHOOSE_1 = (By.XPATH, '//*[@aria-label="Choose воскресенье, 29-е декабря 2024 г."]')
    PHOLD_DATA_CHOOSE_2 = (By.XPATH, '//*[@aria-label="Choose пятница, 13-е декабря 2024 г."]')

    RENTAL_PERIOD = (By.CLASS_NAME, 'Dropdown-arrow') #стрелка выбора периода
    RENTAL_1_DAYS = (By.XPATH, '//*[contains(@class, "Dropdown-option") and text()="сутки"]')
    RENTAL_5_DAYS = (By.XPATH, '//*[contains(@class, "Dropdown-option") and text()="пятеро суток"]')


    POINT_BLACK = (By.ID, "black")
    POINT_GREY = (By.ID, "grey")
    PHOLD_COMMENT = (By.XPATH, '//*[@placeholder="Комментарий для курьера"]')

    BUTTON_ORDER_UP = (By.XPATH, '//*[contains(@class, "Button_Button__ra12g") and text()="Заказать"]')  #кнопка "заказать" вверху на главной
    BUTTON_ORDER_DOWN = (By.CLASS_NAME, "Button_Button__ra12g Button_UltraBig__UU3Lp")  #кнопка "заказать" внизу на главной

    BUTTON_COOKIE = (By.ID, "rcc-confirm-button")

    BUTTON_ORDER_UP_2 = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/button[1]') #кнопка заказть на второй странице заказа сверху
    BUTTON_ORDER_DOWN_2 = (By.XPATH, '//*[contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]') #кнопка заказть на второй странице заказа снизу

    BUTTON_YES = (By.XPATH, '//*[contains(@class, "Button_Middle__1CSJM") and text()="Да"]') #Кнопка "да" при оформлении
    BUTTON_NEXT = (By.XPATH, '//*[contains(@class, "Button_Middle__1CSJM") and text()="Далее"]')  # Кнопка "далее" при оформлении

    SIGNAL_ORDER_IS_READY_2 = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    SIGNAL_ORDER_IS_READY = (By.XPATH, '//*div[2]/div[5]/div[1]')

    BUTTON_SEE_STATUS = (By.XPATH, '//*[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM") and text()="Посмотреть статус"]')

    BUTTON_CLOSE = (By.XPATH, '//*[contains(@class, "la7e715f7") and contains(@class, "o5cd7bebb") and contains(@class, "y799ed6f1")]')
    PHOLD_IN = (By.XPATH, '//*[@aria-label="Войти"]')
    PIN = (By.ID, "ya-search-iframe-283dku")




