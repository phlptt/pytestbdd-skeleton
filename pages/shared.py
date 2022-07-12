from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class Shared(BasePage):
    ACCEPT_COOKIES = "ccc-recommended-settings"  # ID

    def click_accept_cookies(self):
        self.driver.find_element(By.ID, value=Shared.ACCEPT_COOKIES).click()
