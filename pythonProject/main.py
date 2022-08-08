from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/")

driver.implicitly_wait(0.5)
i = 0
while i < 1000:
    search_box = driver.find_element(by=By.XPATH, value="/html/body/form/textarea")
    search_button = driver.find_element(by=By.XPATH, value='/html/body/form/input')
    search_box.clear()
    search_box.send_keys('https://www.youtube.com/')
    search_button.click()
    search_button = driver.find_element(by=By.XPATH, value='/html/body/form/input')
    search_button.click()
    i += 1
