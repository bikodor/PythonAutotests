from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    summa = int(x) + int(y)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(summa))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()



finally:
    time.sleep(5)
    browser.quit()






