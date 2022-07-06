#create web driver
from selenium import webdriver
from selenium.webdriver.common.by import By
#allows webdriver to perform more complex tasks (drag and drop)
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
#maximize browser window size
driver.maximize_window()
#get website
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
#find source element by xpath
source = driver.find_element(By.XPATH, '//*[@id="box3"]')
#destination to drag too
destination = driver.find_element(By.XPATH, '//*[@id="box103"]')
#create action (drag and drop)
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
