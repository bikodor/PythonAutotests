import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    first_name_field = browser.find_element(By.NAME, "firstname")
    first_name_field.send_keys("John")
    last_name_field = browser.find_element(By.NAME, "lastname")
    last_name_field.send_keys("Johnson")
    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys("tralala@gmail.com")
    file_field = browser.find_element(By.ID, "file")
    file_field.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
