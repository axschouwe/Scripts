#install selenium package and  geckodriver for firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
#browser to use
driver = webdriver.Firefox()
#selenium get request 
driver.get('https://www.google.com/')
#xpath to search field
searchField = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
#selenum write funcion in search string
searchField.send_keys('kitties')
#xpath to search button
searchButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
#selenium fuction to click button
searchButton.click()