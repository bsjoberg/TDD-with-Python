from selenium import webdriver
from hamcrest import equal_to, assert_that

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert_that(browser.title, equal_to('Welcome to Django'))
