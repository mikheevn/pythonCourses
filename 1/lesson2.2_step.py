from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
def scrolling(dr, toelem):
    dr.execute_script("arguments[0].scrollIntoView(true)", toelem)


driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get("http://suninjuly.github.io/execute_script.html")

btn = driver.find_element(By.CSS_SELECTOR, "button.btn")

#num1 = int(driver.find_element(By.ID, "num1").text)
#num2 = int(driver.find_element(By.ID, "num2").text)
numb = calc(driver.find_element(By.ID, "input_value").text)

myinput = driver.find_element(By.ID, "answer")
scrolling(driver, myinput)
myinput.send_keys(numb)

scrolling(driver, driver.find_element(By.ID, "robotCheckbox"))
driver.find_element(By.ID, "robotCheckbox").click()
scrolling(driver, driver.find_element(By.ID, "robotsRule"))
driver.find_element(By.ID, "robotsRule").click()

scrolling(driver, btn)
btn.click()

#myselect = Select(driver.find_element(By.CLASS_NAME, "custom-select"))
#myselect.select_by_value(str(num1+num2))

#driver.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(5)
driver.quit()
