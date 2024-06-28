import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(url='http://127.0.0.1:8000/admin/')


def element_is_clickable():
    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys("*")
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys("*")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="user-tools"]/a[1]').click()


def response_check(w, file):
    height = 768
    driver.set_window_size(w, height)
    driver.save_screenshot(file)
