import pytest
import time

from selenium import webdriver
from selenium.common import exceptions

TP_USERNAME = 'nick@plusqa.com'
TP_PASSWORD = 'g5rfCUrcw4Pwq7P'


def wait_until_success(cb, *args, tries=3, interval=1, **kwargs):
    exception = None
    for i in range(tries):
        try:
            return cb(*args, **kwargs)
        except exceptions.WebDriverException as err:
            exception = err
        time.sleep(interval)
    raise exception


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.get('https://testplatform.plusqa.com/')
    wait_until_success(d.find_element_by_id, 'user_email')
    d.find_element_by_id('user_email').send_keys(TP_USERNAME)
    d.find_element_by_id('user_password').send_keys(TP_PASSWORD)
    yield d
    d.close()
