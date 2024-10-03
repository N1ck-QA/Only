from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, app):
        self.app = app

    def _find_clickable_element(self, locator, wait_time=20):
        """
        Find the clickable element. Use Explicit wait
        :param locator: locator like (By.XPATH, 'name')
        :param wait_time: wait time
        :return: return selenium element
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.element_to_be_clickable(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def _find_existing_element(self, locator, wait_time=20):
        """
        Find an existing element. Use Explicit wait
        :param locator: locator like (By.XPATH, 'name')
        :param wait_time: wait time
        :return: return selenium element
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def move_to_element(self, locator, wait_time=20):
        """
        Find an existing element. Use Explicit wait
        :param locator: locator like (By.XPATH, 'name')
        :param wait_time: wait time
        :return: return perform move to element action
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        move = ActionChains(self.app.driver).move_to_element(element)
        return move.perform()

    def click_element(self, locator, wait_time=20):
        """
        Click element.
        """
        element = self._find_clickable_element(locator, wait_time)
        element.click()

    def move_to_end_page(self, locator, wait_time=20):
        """
        move to end page using Keys
        """
        element = self._find_existing_element(locator, wait_time)
        element.send_keys(Keys.END)

    def text(self, locator, wait_time=20) -> str:
        """
        Get element text.
        """
        element = self._find_clickable_element(locator, wait_time)
        return element.text

    def open_page(self, url: str):
        """
        Open page.
        """
        self.app.driver.get(url)
