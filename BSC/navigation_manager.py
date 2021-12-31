import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from SpreadsheetDictionary import bsc_id_dictionary
#from webdriver_manager.chrome import ChromeDriverManager

from SpreadsheetDictionary import bsc_login, bsc_password
import time
import csv

PATH = "/usr/bin/chromedriver"

def init_login(driver): 
    #driver = webdriver.Chrome(PATH)
    driver.get("https://bscpro.com/auth/login")
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-1"))
    )


    #LOGIN PAGE
    login_box = main.find_element_by_name('login')
    #print(login_box.getTagName())
    login_box.send_keys(bsc_login)

    password_box = main.find_element_by_name('password')
    # password_box.click()
    password_box.send_keys(bsc_password)
    password_box.send_keys(Keys.ENTER)

def account_switch(driver, account_number):
    driver.get("https://bscpro.com/auth/login_as_authorized_user/{account_number}")

def production_tracker(driver):
    driver.get("https://bscpro.com/production_new")

def production_add(driver):
      driver.get("https://bscpro.com/add_production")

def prospect_tracker(driver):
    driver.get("https://bscpro.com/prospects_new")
    