from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Path: form_script.py

webdriver_path = 'your/path/to/chromedriver.exe' 
# ^^^^ replace this with your path to chromedriver.exe by coppying the file path *make sure theres no backslashes only forward for python purposes^^^^

driver = webdriver.Chrome()

# url to the scholarship application
url = 'https://www.pointpark.edu/about/admindepts/academicandstudent/scholarshipapplication/index' 
driver.get(url)

# lil delay, gotta take things slow, enjoy life
time.sleep(2)

# elements
first_name_element = driver.find_element(By.NAME, 'field_9409')
last_name_element = driver.find_element(By.NAME, 'field_34927')
student_id_element = driver.find_element(By.NAME, 'field_9410')
student_type_radio_element = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[3]/div/div[2]/form/fieldset[1]/div/div[2]/div[1]/label[1]/input')
student_athlete_radio_element = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[3]/div/div[2]/form/fieldset[2]/div/div[2]/div[1]/label[2]/input')
working_parent_radio_element = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[3]/div/div[2]/form/fieldset[3]/div/div[2]/div[1]/label[2]/input')
major_element = driver.find_element(By.NAME, 'field_9411')
home_address_element = driver.find_element(By.NAME, 'field_9412')
home_country_element = driver.find_element(By.NAME, 'field_44525')
city_element = driver.find_element(By.NAME, 'field_44063')
state_dropdown = Select(driver.find_element(By.NAME, 'field_44064'))

zip_element = driver.find_element(By.NAME, 'field_44065')
phone_element = driver.find_element(By.NAME, 'field_9413')
email_element = driver.find_element(By.NAME, 'field_9414')






# inputs
# Replace these with your own info
first_name_element.send_keys('first name')
last_name_element.send_keys('last name')
student_id_element.send_keys('000000000')
student_type_radio_element.click()
student_athlete_radio_element.click()# radio buttons are fixed for right now, I'll update it later with commented out options
working_parent_radio_element.click()
major_element.send_keys('Applied Computer Science')
home_address_element.send_keys('111 butter street')
home_country_element.send_keys('United States')
city_element.send_keys('city')
desired_state = 'Pennsylvania'
state_dropdown.select_by_visible_text(desired_state) #ignore this don't touch it
zip_element.send_keys('111111')
phone_element.send_keys('0000000000')
email_element.send_keys('email@email.com')


# That should be all for the automated inputs, now just choose which scholarships to apply for and submit


time.sleep(8)

input('Press ENTER to close the automated browser') #via terminal

driver.quit()