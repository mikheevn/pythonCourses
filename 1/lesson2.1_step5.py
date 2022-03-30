from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get("http://suninjuly.github.io/get_attribute.html")

numb = calc(driver.find_element(By.ID, "treasure").get_attribute("valuex"))

myinput = driver.find_element(By.ID, "answer")
myinput.send_keys(numb)

driver.find_element(By.ID, "robotCheckbox").click()
driver.find_element(By.ID, "robotsRule").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()



time.sleep(5)
driver.quit()
