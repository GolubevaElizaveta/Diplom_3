import allure
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.order_page import OrderPage
from page_objects.personal_account_page import PersonalAccountPage
from urls import URLs


class TestOrderFeed:

    @allure.title('Оформление заказа авторизованным пользователем')
    def test_successful_order(self, driver, create_user_fixture):
        if create_user_fixture is None:
            pytest.fail("Не удалось создать пользователя для теста.")

        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        # Авторизация пользователя
        main_page.click_on_login_button()
        login_page.input_login(create_user_fixture['email'])
        login_page.input_password(create_user_fixture['password'])
        login_page.click_on_login_submit_button()

        # Ожидание загрузки главной страницы
        main_page.wait_for_main_page_to_load()

        # Добавление ингредиента в заказ
        main_page.add_ingredient_to_order()

        # Клик на кнопку "Оформить заказ"
        main_page.click_on_submit_order_button()

        # Проверка, что окно заказа отображается и идентификатор заказа виден
        order_id_visible = main_page.order_window_is_visible()
        order_id_text = main_page.get_order_number()

        assert order_id_visible and order_id_text is not None, \
            f"Окно заказа не отображается или идентификатор заказа неверный: {order_id_text}."


    @allure.title('Созданный заказ отображается в ленте заказов')
    def test_order_is_displayed_in_feed_after_creation(self, driver, create_user_fixture):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        # Авторизация пользователя
        main_page.click_on_login_button()
        login_page.input_login(create_user_fixture['email'])
        login_page.input_password(create_user_fixture['password'])
        login_page.click_on_login_submit_button()

        # Ожидание загрузки главной страницы
        main_page.wait_for_main_page_to_load()

        # Добавление ингредиента в заказ
        main_page.add_ingredient_to_order()

        # Оформление заказа
        main_page.click_on_submit_order_button()
        main_page.close_order_window()

        # Переход на страницу "Лента заказов"
        main_page.click_on_personal_account_button(URLs.PERSONAL_ACCOUNT_PAGE)
        personal_account_page.click_on_order_history_button(URLs.ORDER_HISTORY_PAGE)

        # Получение номера созданного заказа из истории
        created_order_number = personal_account_page.get_order_number_from_orders_history()

        # Переход обратно в ленту заказов
        personal_account_page.click_on_order_feed_button(URLs.ORDER_PAGE)

        # Проверка, что заказ отображается в ленте заказов
        assert order_page.is_order_number_in_list(created_order_number), \
            f"Созданный заказ {created_order_number} не отображается в ленте заказов."

    @allure.title('Создание заказа увеличивает общий счетчик заказов')
    def test_order_creation_updates_all_time_counter(self, driver, create_user_fixture):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_fixture['email'])
        login_page.input_password(create_user_fixture['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_for_main_page_to_load()
        main_page.click_on_order_feed_button(URLs.ORDER_PAGE)

        order_feed_page = OrderPage(driver)
        initial_orders_amount = order_feed_page.get_all_time_counter_number()
        order_feed_page.click_on_constructor_button(URLs.BASE_URL)

        main_page.add_ingredient_to_order()
        main_page.click_on_submit_order_button()
        main_page.close_order_window()
        main_page.click_on_order_feed_button(URLs.ORDER_PAGE)
        all_time_counter_increased = order_feed_page.is_all_time_counter_increased(initial_orders_amount)
        assert all_time_counter_increased, "Ошибка: Общий счетчик заказов не увеличился после создания нового заказа."

    @allure.title('Создание заказа увеличивает счетчик заказов за сегодня')
    def test_order_creation_updates_today_counter(self, driver, create_user_fixture):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_fixture['email'])
        login_page.input_password(create_user_fixture['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_for_main_page_to_load()
        main_page.click_on_order_feed_button(URLs.ORDER_PAGE)

        order_feed_page = OrderPage(driver)
        initial_orders_amount = order_feed_page.get_today_counter_number()
        order_feed_page.click_on_constructor_button(URLs.BASE_URL)

        main_page.add_ingredient_to_order()
        main_page.click_on_submit_order_button()
        main_page.close_order_window()
        main_page.click_on_order_feed_button(URLs.ORDER_PAGE)
        today_counter_increased = order_feed_page.is_today_counter_increased(initial_orders_amount)
        assert today_counter_increased

    @allure.title('Созданный заказ отображается в разделе "В работе"')
    def test_created_order_shows_in_work_orders(self, driver, create_user_fixture):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_fixture['email'])
        login_page.input_password(create_user_fixture['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_for_main_page_to_load()
        main_page.add_ingredient_to_order()
        main_page.click_on_submit_order_button()

        created_order_number = main_page.get_order_number()
        main_page.close_order_window()
        main_page.click_on_order_feed_button(URLs.ORDER_PAGE)

        order_feed_page = OrderPage(driver)

        # Ожидание появления заказа в разделе "В работе"
        order_feed_page.wait_for_order_to_appear(created_order_number)

        # Проверяем, что заказ отображается в разделе "В работе"
        assert order_feed_page.is_order_number_in_work_list(created_order_number), \
            f"Созданный заказ {created_order_number} не отображается в разделе 'В работе'."