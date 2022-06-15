from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver

    driver.close()
    driver.quit()
