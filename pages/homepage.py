from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):
    GET_IN_TOUCH_LINK = ".header__get-in-touch"  # CSS

    def click_get_in_touch(self):
        self.driver.find_element(By.CSS_SELECTOR, value=HomePage.GET_IN_TOUCH_LINK).click()
