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
import time
import csv

# driver = webdriver.Chrome(ChromeDriverManager().install())
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)



def download_production(driver):

    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-1"))
    )

    time.sleep(5)

    # for user in driver.find_elements_by_class_name('loginas_users_div loginas_user'):
    #     if user.find

    #Goes to Production Tracker
    driver.get("https://bscpro.com/production_new")

    time.sleep(5)

    driver.current_url

    calendar_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[7]/div[1]/div/div[2]/div/div[1]/div/input')
    calendar_button.click()


    #daterangepicker ltr auto-apply show-ranges show-calendar opensleft
    #range
    #LI All
    calendar_all_button = driver.find_element_by_xpath('/html/body/div[10]/div[1]/ul/li[1]')
    calendar_all_button.click()

    time.sleep(30)

    production_excel_button = driver.find_element_by_id('excel_export')
    production_excel_button.click()
    time.sleep(30)

    # calendar_button = driver.find_element_by_class_name('fa fa-calendar')
    # calendar_button.click()

    # calendar_all_button = driver.find_element_by_xpath('/html/body/div[8]/div[1]/ul/li[1]')
    # calendar_all_button.click()

    # time.sleep(30)

# def main():
#     download_production()

# if __name__ == "__main__":
#     main()