from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
def scrolling(dr, toelem):
    dr.execute_script("arguments[0].scrollIntoView(true)", toelem)


driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

btn = driver.find_element(By.CSS_SELECTOR, "button.btn")
btn.click()


numb = calc(driver.find_element(By.ID, "input_value").text)
myinput = driver.find_element(By.ID, "answer")
myinput.send_keys(numb)

driver.find_element(By.ID, "solve").click()


time.sleep(5)
driver.quit()
