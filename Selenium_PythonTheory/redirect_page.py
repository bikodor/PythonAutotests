import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

try:
    travel = browser.find_element(By.TAG_NAME, "button")
    travel.click()
    new_window = browser.window_handles[1]
    # first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
