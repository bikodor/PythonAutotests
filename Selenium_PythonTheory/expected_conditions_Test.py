import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    price = WebDriverWait(browser, 12).until\
        (EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()