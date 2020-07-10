import logging
from selenium import webdriver


def test_chromedriver_opens(driver: webdriver.Chrome):
    driver.find_element_by_xpath('//*')
    window_size = driver.get_window_size()
    logging.info('Window size: %s', window_size)
