#wait functions add crucial time intervals in between actions performed (selenium trying to click, before a link is loaded)
#explicit and implicit waits in selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.google.com'
driver = webdriver.Firefox()
driver.get(url)
#create webdriver wait time (10 seconds)
wait = WebDriverWait(driver, 10)
#xpath to search field
searchField = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
#imput string search field
searchField.send_keys('Hello World')

#wait until expected contidtions module is True, and the xpath of the button
clickButton = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')))
#click button after conditions are met
clickButton.click()

