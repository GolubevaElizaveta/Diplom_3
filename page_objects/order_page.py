from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage
from locators.order_feed_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import allure
import time

class OrderPage(BasePage):
    @allure.step("Проверка заголовка 'Лента заказов'")
    def is_order_feed_header_visible(self):
        try:
            header = self.find_element_with_wait(OrderPageLocators.ORDER_FEED_HEADER)
            return header.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step("Нажатие на кнопку 'Конструктор'")
    def click_on_constructor_button(self, url):
        constructor_button = self.find_element_with_wait(MainPageLocators.CONSTRUCTOR)
        self.click_on_element_js(constructor_button)
        self.wait_for_url_to_be(url)
        return self.get_current_url()

    @allure.step("Открыть заказ")
    def click_on_order(self):
        order = self.find_element_with_wait(OrderPageLocators.ORDER)
        self.click_on_element_js(order)

    @allure.step("Проверка видимости окна деталей заказа")
    def order_details_window_is_visible(self):
        try:
            # Проверка видимости окна деталей заказа
            order_details_window = self.find_element_with_wait(OrderPageLocators.ORDER_DETAILS_WINDOW)
            if order_details_window.is_displayed():
                # Проверка заголовка окна
                header_text = self.get_text_from_element(MainPageLocators.ORDER_DETAILS_MODAL)  # Убедитесь, что локатор правильный
                expected_header = "Ожидаемый текст заголовка"  # Укажите ожидаемый текст заголовка
                return header_text == expected_header  # Возвращаем True, если заголовок соответствует
            return False
        except (TimeoutException, NoSuchElementException):
            return False


    @allure.step("Проверка наличия номера заказа в списке всех заказов")
    def is_order_number_in_list(self, order_number):
        order_elements = self.find_elements_with_wait(OrderPageLocators.ORDER_LIST)

        for _ in order_elements:
            order_number_text = self.get_text_from_element(OrderPageLocators.ORDER_LIST_NUMBERS)
            if order_number_text == order_number:
                return True
        return False

    @allure.step("Получение номера счетчика выполненных заказов за все время")
    def get_all_time_counter_number(self):
        self.find_element_with_wait(OrderPageLocators.ALL_TIME_COUNTER)
        all_time_counter = self.get_text_from_element(OrderPageLocators.ALL_TIME_COUNTER)
        return all_time_counter

    @allure.step("Проверка увеличения счетчика выполненных заказов за все время")
    def is_all_time_counter_increased(self, initial_counter):
        current_counter = self.get_all_time_counter_number()
        return int(current_counter) > int(initial_counter)

    @allure.step("Получение номера счетчика выполненных заказов за сегодня")
    def get_today_counter_number(self):
        self.find_element_with_wait(OrderPageLocators.TODAY_COUNTER)
        today_counter = self.get_text_from_element(OrderPageLocators.TODAY_COUNTER)
        return today_counter

    @allure.step("Проверка увеличения счетчика выполненных заказов за сегодня")
    def is_today_counter_increased(self, initial_counter):
        current_counter = self.get_today_counter_number()
        return int(current_counter) > int(initial_counter)

    @allure.step("Ожидание появления заказа в списке заказов 'В работе'")
    def wait_for_order_to_appear(self, order_number):
        end_time = time.time() + 30
        while time.time() < end_time:
            if self.is_order_number_in_work_list(order_number):
                return
            time.sleep(1)
        raise AssertionError(f"Заказ {order_number} не появился в списке 'В работе' за 30 секунд.")

    @allure.step("Проверка наличия номера заказа в списке 'В работе'")
    def is_order_number_in_work_list(self, order_number):
        orders_section = self.find_elements_with_wait(OrderPageLocators.IN_WORK_ORDERS)
        for order in orders_section:
            order_text = order.text[1:]
            if order_text == order_number:
                return True
        return False