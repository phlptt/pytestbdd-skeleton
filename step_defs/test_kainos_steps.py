from pytest_bdd import given, when, then, scenarios
from pages.shared import Shared
from pages.homepage import HomePage
from pages.contact_us import ContactUs

scenarios("../features/kainos.feature")


@given("I visit Kainos homepage")
def visit_homepage(browser):
    browser.get("http://www.kainos.com")


@when("I go to get in touch")
def go_to_get_in_touch(browser):
    HomePage(browser).click_get_in_touch()


@when("I accept cookies")
def accept_cookies(browser):
    Shared(browser).click_accept_cookies()


@then("I am on contact us")
def assert_get_in_touch(browser):
    assert ContactUs(browser).get_expected_title() in browser.title
