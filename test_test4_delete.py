
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Chrome()


driver.get("http://127.0.0.1:2000/categories")
driver.set_window_size(1552, 832)
driver.find_element(By.LINK_TEXT, "Delete").click()
driver.find_element(By.CSS_SELECTOR, "body").click()
driver.find_element(By.CSS_SELECTOR, "body").click()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.double_click(element).perform()
assert driver.find_element(By.CSS_SELECTOR, "body").text == "deleted"
  
