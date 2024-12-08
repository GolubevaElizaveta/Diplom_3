from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderPageLocators
import allure


class MainPage(BasePage):
    @allure.step("Нажатие на кнопку 'Конструктор'")
    def click_on_constructor_button(self, url):
        constructor_button = self.find_element_with_wait(MainPageLocators.CONSTRUCTOR)
        self.click_on_element_js(constructor_button)
        self.wait_for_url_to_be(url)
        return self.get_current_url()

    @allure.step("Проверка заголовка 'Соберите бургер'")
    def is_constructor_header_visible(self):
        try:
            header = self.find_element_with_wait(MainPageLocators.MAIN_PAGE)
            return header.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step("Нажатие на кнопку 'Войти в аккаунт'")
    def click_on_login_button(self):
        try:
            login_button = self.find_element_with_wait(MainPageLocators.LOGIN_BUTTON)
            if login_button:
                self.click_on_element_js(login_button)
            else:
                raise Exception("Кнопка 'Войти в аккаунт' не найдена.")
        except TimeoutException:
            print("Не удалось найти кнопку 'Войти в аккаунт' за отведенное время.")

    def wait_for_main_page_to_load(self):
        try:
            self.find_element_with_wait(MainPageLocators.MAIN_PAGE)
        except TimeoutException:
            print("Главная страница не загрузилась за отведенное время.")

    @allure.step("Нажатие на кнопку 'Личный кабинет'")
    def click_on_personal_account_button(self, url):
        try:
            personal_account_button = self.find_element_with_wait(MainPageLocators.PERSONAL_ACCOUNT)
            if personal_account_button:
                self.click_on_element_js(personal_account_button)
            else:
                raise Exception("Кнопка 'Личный кабинет' не найдена.")
            self.wait_for_url_to_be(url)
            return self.get_current_url()
        except Exception as e:
            print(f"Ошибка при клике на кнопку 'Личный кабинет': {e}")
            return None

    @allure.step("Нажатие на кнопку 'Лента заказов'")
    def click_on_order_feed_button(self, url):
        try:
            order_feed_button = self.find_element_with_wait(MainPageLocators.ORDER_FEED)
            if order_feed_button:
                self.click_on_element_js(order_feed_button)
                self.wait_for_url_to_be(url)
                return self.get_current_url()
            else:
                raise Exception("Кнопка 'Лента заказов' не найдена.")
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при клике на кнопку 'Лента заказов': {e}")
            return None

    @allure.step("Нажатие на ингредиент")
    def click_on_ingredient(self):
        try:
            ingredient = self.find_element_with_wait(MainPageLocators.INGREDIENT)
            self.click_on_element_js(ingredient)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при клике на ингредиент: {e}")

    @allure.step("Проверка видимости окна деталей ингредиента")
    def is_ingredient_details_window_visible(self):
        try:
            ingredient_details_window = self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS_MODAL)
            if ingredient_details_window.is_displayed():
                header_text = self.get_text_from_element(MainPageLocators.INGREDIENT_DETAILS_MODAL)
                expected_header = "Детали ингредиента"  # Убедитесь, что это значение актуально
                return header_text == expected_header  # Возвращаем True, если заголовок соответствует
            return False
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step("Закрытие окна деталей ингредиента")
    def close_ingredient_details_window(self):
        try:
            close_button = self.find_element_with_wait(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)
            self.click_on_element_js(close_button)
            modal_element = self.find_element_with_wait(MainPageLocators.ACTIVE_MODAL)
            return 'Modal_modal_opened__3ISw4' not in modal_element.get_attribute('class')
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при закрытии окна деталей ингредиента: {e}")
            return False

    @allure.step("Перемещение ингредиента в корзину")
    def add_ingredient_to_order(self):
        try:
            source = self.find_element_with_wait(MainPageLocators.INGREDIENT)
            target = self.find_element_with_wait(MainPageLocators.BASKET)
            self.move_elements(source, target)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при перемещении ингредиента: {e}")

    @allure.step("Проверка увеличения счетчика ингредиента")
    def is_ingredient_counter_increased(self):
        try:
            self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER)
            counter_text = self.get_text_from_element(MainPageLocators.INGREDIENT)
            return counter_text != '0'
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при проверке счетчика ингредиента: {e}")
            return False

    @allure.step("Клик на кнопку 'Оформить заказ'")
    def click_on_submit_order_button(self):
        try:
            submit_order_button = self.find_element_with_wait(MainPageLocators.SUBMIT_ORDER_BUTTON)
            self.click_on_element_js(submit_order_button)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при клике на кнопку 'Оформить заказ': {e}")

    @allure.step("Проверка видимости окна заказа")
    def order_window_is_visible(self):
        try:
            order_window = self.find_element_with_wait(MainPageLocators.ORDER_MODAL)
            return order_window.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step("Закрытие окна заказа")
    def close_order_window(self):
        try:
            close_button = self.find_element_with_wait(MainPageLocators.CLOSE_ORDER_MODAL_BUTTON)
            self.click_on_element_js(close_button)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при закрытии окна заказа: {e}")

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        try:
            # Ожидаем, пока текст номера заказа изменится с '9999'
            self.wait_for_text_to_change(MainPageLocators.ORDER_NUMBER, '9999')

            # Ожидаем, пока сообщение о подготовке заказа станет видимым
            self.wait_for_element_to_be_clickable(OrderPageLocators.ORDER_PREPARATION_MESSAGE)

            # Получаем актуальный номер заказа
            order_number = self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
            return order_number
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Ошибка при получении номера заказа: {e}")
            return None
