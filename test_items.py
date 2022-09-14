import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/'


def test_find_add_to_cart_button(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket'), 'Кнопка не найдена'

