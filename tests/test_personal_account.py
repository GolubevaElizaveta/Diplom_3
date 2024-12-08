import allure
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.personal_account_page import PersonalAccountPage
from urls import URLs

class TestPersonalAccount:
    @allure.title("Проверка доступа к личному кабинету после входа")
    def test_access_personal_account_with_profile_check(self, driver, create_user_fixture):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)

        login_page.input_login(create_user_fixture['email'])
        login_page.input_password(create_user_fixture['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_for_main_page_to_load()
        actual_url = main_page.click_on_personal_account_button(URLs.PERSONAL_ACCOUNT_PAGE)

        personal_account_page = PersonalAccountPage(driver)
        profile_visible = personal_account_page.is_profile_link_visible()

        assert actual_url == URLs.PERSONAL_ACCOUNT_PAGE and profile_visible, f"Expected URL: {URLs.PERSONAL_ACCOUNT_PAGE}, but got: {actual_url}. Profile link visible: {profile_visible}."

    @allure.title("Переход на страницу 'История заказов' из личного кабинета")
    def test_navigate_to_order_history_successful(self, driver, create_user_fixture):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)

        login_page.input_login(create_user_fixture['email'])
        login_page.input_password(create_user_fixture['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_for_main_page_to_load()
        main_page.click_on_personal_account_button(URLs.PERSONAL_ACCOUNT_PAGE)
        personal_account_page = PersonalAccountPage(driver)
        actual_url = personal_account_page.click_on_order_history_button(URLs.ORDER_HISTORY_PAGE)
        assert actual_url == URLs.ORDER_HISTORY_PAGE, \
            f"Expected URL: {URLs.ORDER_HISTORY_PAGE}, but got: {actual_url}."

    @allure.title("Выход из аккаунта")
    def test_logout_from_personal_account(self, driver, create_user_fixture):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)

        login_page.input_login(create_user_fixture['email'])
        login_page.input_password(create_user_fixture['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_for_main_page_to_load()
        main_page.click_on_personal_account_button(URLs.PERSONAL_ACCOUNT_PAGE)
        personal_account_page = PersonalAccountPage(driver)
        actual_url = personal_account_page.logout(URLs.LOGIN_PAGE)
        login_header_visible = personal_account_page.is_login_header_visible()

        assert actual_url == URLs.LOGIN_PAGE and login_header_visible, \
            f"Expected URL: {URLs.LOGIN_PAGE}, but got: {actual_url}. " \
            f"Login header visibility: {login_header_visible}."