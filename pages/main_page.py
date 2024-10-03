from pages.base_page import BasePage
from constants import Locators


class MainPage(BasePage):

    def open_main_page(self):
        """
        Open main page.
        """
        self.open_page(self.app.url)

    def click_button_to_accept_cookie(self):
        """
        Accept 'Cookies'
        """
        self.click_element(locator=Locators.ACCEPT_COOKIE)

    def scroll_page_to_end(self):
        """
        Scroll page to end
        """
        self.move_to_end_page(locator=Locators.HTML)

    def footer_exist(self):
        """
        Looking for element 'footer' on the page
        """
        self._find_existing_element(locator=Locators.FOOTER)

    def text_from_vk_link(self):
        """
        Get text from vk link in the footer
        """
        element = self.text(locator=Locators.BUTTON_VK)
        return element

    def click_button_company(self):
        """
        Open 'Компания' tab (page) via main page
        """
        self.click_element(locator=Locators.BUTTON_COMPANY)

    def click_button_career(self):
        """
        Open 'Карьера' tab (page) via main page
        """
        self.click_element(locator=Locators.BUTTON_CAREER)

    def text_from_start_project_button(self):
        """
        Get text from "Начать проект" button in the footer
        """
        element = self.text(locator=Locators.BUTTON_START)
        return element

    def text_from_telegram_link(self):
        """
        Get text from "Telegram" link in the footer
        """
        element = self.text(locator=Locators.TELEGRAM)
        return element

    def text_from_email_button(self):
        """
        Get text "hello@only.com.ru" in the footer
        """
        element = self.text(locator=Locators.EMAIL)
        return element
