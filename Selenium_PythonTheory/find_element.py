# find_element(By.ID, value)
# find_element(By.CSS_SELECTOR, value)
# find_element(By.XPATH, value)
# find_element(By.NAME, value)
# find_element(By.TAG_NAME, value)
# find_element(By.CLASS_NAME, value)
# find_element(By.LINK_TEXT, value)
# find_element(By.PARTIAL_LINK_TEXT, value)


from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    browser.quit()

# browser.close()
# browser.quit()

