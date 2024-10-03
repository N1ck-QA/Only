from selenium.webdriver.common.by import By


class Locators:
    HTML = (By.XPATH, '//main')
    ACCEPT_COOKIE = (By.XPATH, "//button[@class='sc-dd76fd40-3 jopRme']")
    FOOTER = (By.XPATH, '//main/div[1]/footer')
    BUTTON_VK = (By.XPATH, '//main//span[contains(text(), "Vkontakte")]')
    BUTTON_START = (By.XPATH, '//main//p[contains(text(), "Начать проект")]')
    BUTTON_COMPANY = (By.XPATH, '//*[@id="Header"]//span[contains(text(), "Компания")]')
    TELEGRAM = (By.XPATH, '//main//span[contains(text(), "Telegram")]')
    BUTTON_CAREER = (By.XPATH, '//*[@id="Header"]//span[contains(text(), "Карьера")]')
    EMAIL = (By.XPATH, '//main//p[contains(text(), "hello@only.com.ru")]')
