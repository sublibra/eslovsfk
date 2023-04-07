from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from decouple import config
import pysftp
import os

## Login idrottonline
firefox_options = Options()
firefox_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service('/usr/local/bin/geckodriver'), options=firefox_options)
driver.get('https://login.idrottonline.se')
user_name = driver.find_element(By.ID, 'userName') 
user_name.send_keys(config('IDROTT-USER'))
password = driver.find_element(By.NAME, 'password') 
password.send_keys(config('IDROTT-PASS'))
submit = driver.find_element(By.XPATH, "//form/button") #loginForm > button
submit.click()
time.sleep(7) ## Many many redirects

## Export calendar
calendar_string = "https://activity.idrottonline.se/activities/exportactivitiestoical?calendarId=7140&startTime={0}-01-01+00%3A00%3A00&endTime={0}-12-31+00%3A00%3A00&freeText=&activityTypes="
driver.get(calendar_string.format(datetime.today().strftime('%Y')))
time.sleep(4) ## Wait for file
driver.quit()

## Copy file to home page
cal_file = os.path.expanduser( '~' ) + '/Downloads/Kalender.ics'
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
if os.path.exists(cal_file):
  with pysftp.Connection(config('SFTP-HOST'), username=config('SFTP-USER'), password=config('SFTP-PASS'), cnopts=cnopts) as sftp:
   with sftp.cd('wp-content/uploads'): 
      sftp.put(cal_file)  
  os.remove(cal_file)
else:
  print('Failed to retrieve or find the file: {0}'.format(cal_file))
