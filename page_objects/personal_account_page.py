import allure
from page_objects.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators
from locators.main_page_locators import MainPageLocators


class PersonalAccountPage(BasePage):
    @allure.step("Проверка наличия 'Профиль'")
    def is_profile_link_visible(self):
        try:
            profile_link = self.find_element_with_wait(PersonalAccountPageLocators.PROFILE_LINK)
            return profile_link.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step("Переход по названию 'История заказов'")
    def click_on_order_history_button(self, url):
        order_history = self.find_element_with_wait(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)
        self.click_on_element_js(order_history)
        self.wait_for_url_to_be(url)
        return self.get_current_url()

    @allure.step("Выход из личного кабинета")
    def logout(self, url):
        logout_button = self.find_element_with_wait(PersonalAccountPageLocators.LOGOUT_BUTTON)
        self.click_on_element_js(logout_button)
        self.wait_for_url_to_be(url)
        return self.get_current_url()

    @allure.step("Нажатие на кнопку 'Лента заказов'")
    def click_on_order_feed_button(self, url):
        order_feed_button = self.find_element_with_wait(MainPageLocators.ORDER_FEED)
        self.click_on_element_js(order_feed_button)
        self.wait_for_url_to_be(url)

    @allure.step("Получение номера заказа из истории заказов")
    def get_order_number_from_orders_history(self):
        self.find_element_with_wait(PersonalAccountPageLocators.LAST_ORDER_NUMBER)
        order_number = self.get_text_from_element(PersonalAccountPageLocators.LAST_ORDER_NUMBER)
        return order_number

    @allure.step("Проверка наличия заголовка 'Вход'")
    def is_login_header_visible(self):
        try:
            header = self.find_element_with_wait(PersonalAccountPageLocators.LOGIN_TITLE_LOCATOR)
            return header.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False