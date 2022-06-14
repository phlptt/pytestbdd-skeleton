from pages.BasePage import BasePage


class Shared(BasePage):
    ACCEPT_COOKIES = "ccc-recommended-settings"  # ID

    def click_accept_cookies(self):
        self.driver.find_element_by_id(Shared.ACCEPT_COOKIES).click()
