from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from urls import URLs
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.recovery_password_page import RecoverPasswordPage
import allure


class TestRecoveryPassword:

    def test_navigate_to_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button(URLs.LOGIN_PAGE)
        login_page = LoginPage(driver)
        actual_url = login_page.click_on_recover_password_button()
        recover_password_page = RecoverPasswordPage(driver)
        assert actual_url == URLs.FORGOT_PASS_PAGE and recover_password_page.is_recovery_password_header_visible(), \
            f"Expected URL: {URLs.FORGOT_PASS_PAGE}, but got: {actual_url}. Заголовок 'Восстановление пароля' не найден."

    @allure.title('Ввод email и переход на страницу сброса пароля')
    def test_password_recovery_with_email_input(self, driver, create_user_fixture):
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button(URLs.LOGIN_PAGE)
        login_page = LoginPage(driver)
        login_page.click_on_recover_password_button()
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.input_email(create_user_fixture['email'])
        actual_url = recover_password_page.click_on_recover_button(URLs.RESET_PASS_PAGE)
        assert actual_url == URLs.RESET_PASS_PAGE

    @allure.title('Клик на иконку "Показать пароль" отображает пароль')
    def test_password_visibility_toggle(self, driver, create_user_fixture):
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button(URLs.LOGIN_PAGE)
        login_page = LoginPage(driver)
        login_page.click_on_recover_password_button()
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.input_email(create_user_fixture['email'])
        recover_password_page.click_on_recover_button(URLs.RESET_PASS_PAGE)
        recover_password_page.click_on_view_password()
        assert recover_password_page.is_password_visible()
