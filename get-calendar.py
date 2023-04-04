from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import shutil
from decouple import config
import pysftp


## Login idrottonline
browser = webdriver.Firefox()
browser.get('https://login.idrottonline.se')
user_name = browser.find_element(By.ID, 'userName') 
user_name.send_keys(config('USERNAME'))
password = browser.find_element(By.NAME, 'password') 
password.send_keys(config('PASSWORD'))
submit = browser.find_element(By.XPATH, "//form/button") #loginForm > button
submit.click()
time.sleep(7) ## Many many redirects

## Export calendar
calendar_string = "https://activity.idrottonline.se/activities/exportactivitiestoical?calendarId=7140&startTime={0}-01-01+00%3A00%3A00&endTime={0}-12-31+00%3A00%3A00&freeText=&activityTypes="
browser.get(calendar_string.format(datetime.today().strftime('%Y')))
time.sleep(4) ## Wait for file
browser.close()

## Copy file to home page
#with pysftp.Connection('hostname', username='me', password='secret') as sftp:

## Clean-up
try:
  shutil.rmtree('~/Downloads/Kalender.ics')
except EnvironmentError:
    print("Couldn't delete file")

