import pytest
import os
import time

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

TP_USERNAME = 'nick@plusqa.com'
TP_PASSWORD = 'g5rfCUrcw4Pwq7P'


def wait_until_success(cb, *args, tries=3, interval=1, **kwargs):
    """
    Add a wait until function to selenium webdriver
    :param cb:
    :param args:
    :param tries:
    :param interval:
    :param kwargs:
    :return:
    """
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
    """
    Start the driver and log into TP
    :return:
    """
    if os.getenv('PROD', '').lower() in ['yes', 'true', 't', '1']:
        host_name = os.getenv('HOSTNAME', 'chrome-standalone')
        d = webdriver.Remote(
            command_executor='http://{}:4444/wd/hub'.format(host_name),
            desired_capabilities=DesiredCapabilities.CHROME.copy()
        )
    else:
        d = webdriver.Chrome()
    d.get('https://testplatform.plusqa.com/')
    wait_until_success(d.find_element_by_id, 'user_email')
    d.find_element_by_id('user_email').send_keys(TP_USERNAME)
    d.find_element_by_id('user_password').send_keys(TP_PASSWORD)
    d.find_element_by_xpath('//*[@value="Log In"]').click()
    wait_until_success(d.find_element_by_id, 'graphContainer')
    yield d
    d.close()
