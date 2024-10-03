class TestFooter:

    def test_footer_exist(self, app):
        """
        There's element "footer" on the main page
        """
        app.main_page.open_main_page()  # Открываем основную страницу
        app.main_page.click_button_to_accept_cookie()  # Принимаем cokkie
        app.main_page.scroll_page_to_end()  # Скролим страницу вниз (для наглядности, можно эту строку удалить)
        app.main_page.footer_exist()  # Проверяем наличие элемента footer в DOM-дереве HTML страницы

    def test_vkontakte_is_in_the_footer(self, app):
        """
        There's “Vkontakte” link in the footer on the main page
        """
        app.main_page.open_main_page()  # Открываем основную страницу
        app.main_page.click_button_to_accept_cookie()  # Принимаем cokkie
        app.main_page.scroll_page_to_end()  # Скролим страницу вниз (для наглядности, можно эту строку удалить)
        assert app.main_page.text_from_vk_link() == 'Vkontakte'  # Проверяем наличие ссылки на ВК в footer через получение текста из найденного элемента

    def test_start_project_is_in_the_footer(self, app):
        """
        There's “Начать проект” button in the footer on the main page
        """
        app.main_page.open_main_page()  # Открываем основную страницу
        app.main_page.click_button_to_accept_cookie()  # Принимаем cokkie
        app.main_page.scroll_page_to_end()  # Скролим страницу вниз (для наглядности, можно эту строку удалить)
        assert app.main_page.text_from_start_project_button() == 'Начать проект'  # Проверяем наличие кнопки "Начать проект" в footer через получение текста из найденного элемента

    def test_telegram_link_is_in_the_footer(self, app):
        """
        There's “Telegram” link in the footer on the "about company" page
        """
        app.main_page.open_main_page()  # Открываем основную страницу
        app.main_page.click_button_to_accept_cookie()  # Принимаем cokkie
        app.main_page.click_button_company()  # Открываем страницу https://only.digital/company ("О компании") через кнопку "Компания" на основной странице
        assert app.main_page.text_from_telegram_link() == 'Telegram'  # Проверяем наличие кнопки "Telegtam" в footer через получение текста из найденного элемента

    def test_email_is_in_the_footer(self, app):
        """
        There's Email address in the footer on the "career" page
        """
        app.main_page.open_main_page()  # Открываем основную страницу
        app.main_page.click_button_to_accept_cookie()  # Принимаем cokkie
        app.main_page.click_button_career()  # Открываем страницу https://only.digital/job ("Карьера") через кнопку "Карьера" на основной странице
        assert app.main_page.text_from_email_button() == 'hello@only.com.ru'  # Проверяем наличие кнопки/текста 'hello@only.com.ru' в footer через получение текста из найденного элемента
