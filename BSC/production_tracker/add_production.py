import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from SpreadsheetDictionary import spreadsheet_id_dictionary, range_id_dictionary, person_id_dictionary, SCOPES, SCRIPT_ID, RECIPIENT, bsc_login, bsc_password
#from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
#import gspread

# driver = webdriver.Chrome(ChromeDriverManager().install())
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

# now we can import the module in the parent

#Load Data From Google Sheets
# directory.


def add_production(values):

    #Gets data
    last_row = values[1]

    #Select Data


    # client_name = last_row[0][0] #A

    # # #Need to do this, it requires some work arounds
    # agents = last_row[0][1] #Agent(s) split into two agents B 
    # write_date = last_row[0][2] #C


    # total_points = last_row[0][3] #D
    # product_name = last_row[0][9] #J
    # policy_number = last_row[0][10] #K
    # issued_date = last_row[0][12] #M
    # arrived_date = last_row[0][14] #O
    # agent_date = last_row[0][15] #P
    # pdr_date = last_row[0][16] #Q
    # notes = last_row[0][17] #R


    client_name = last_row[0] #A
    agents = last_row[1] #Agent(s) split into two agents B 
    write_date = last_row[2] #C
    total_points = last_row[3] #D
    product_name = last_row[9] #J
    policy_number = last_row[10] #K
    issued_date = last_row[12] #M
    arrived_date = last_row[14] #O
    agent_date = last_row[15] #P
    pdr_date = last_row[16] #Q
    notes = last_row[17] #R

    split_write_date = write_date.split('-')
    # num_target_month = split_write_date[0]
    num_target_month = '03'
    target_day = split_write_date[1]
    # target_year = split_write_date[2]
    target_year = '2024'

    print(client_name)
    print(agents)
    print(write_date)
    print(num_target_month)
    print(target_day)
    print(target_year)
    # print(total_points)
    # print(product_name)
    # print(policy_number)
    # print(issued_date)
    # print(arrived_date)
    # print(agent_date)
    # print(pdr_date)
    # print(notes)


    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://bscpro.com/auth/login")

    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-1"))
    )


    #LOGIN PAGE
    login_box = main.find_element_by_xpath('/html/body/div/div/div/div/div/div[1]/form/section/div[1]/input')
    login_box.send_keys(bsc_login)

    password_box = main.find_element_by_xpath('/html/body/div/div/div/div/div/div[1]/form/section/div[2]/input')
    password_box.send_keys(bsc_password)
    password_box.send_keys(Keys.ENTER)

    #DASHBOARD, Need to reload elements
    #driver.refresh()
    driver.current_url
    #try:
    # element_to_hover_over = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/ul[3]/li[2]/ul/li[6]/a')
    # hover = ActionChains(driver).move_to_element(element_to_hover_over)
    # hover.perform()
    production_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/ul[3]/li[2]/ul/li[6]/a')
    production_button.click()

    add_product_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/ul[3]/li[2]/ul/li[6]/ul/li[1]/a')
    add_product_button.click()

    driver.current_url
    #written_date_icon = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div/section/div/form/div[1]/div/div[1]/span')
    written_date_icon = driver.find_element_by_class_name('input-group-addon')
    written_date_icon.click()

    target_month = ''
    target_month_abv = ''
    if (num_target_month == '01'):
        target_month = 'January'
        target_month_abv = 'Jan'
    elif (num_target_month == '02'):
        target_month = 'Feburary'
        target_month_abv = 'Feb'
    elif (num_target_month == '03'):
        target_month = 'March'
        target_month_abv = 'Mar'
    elif (num_target_month == '04'):
        target_month = 'April'
        target_month_abv = 'Apr'
    elif (num_target_month == '05'):
        target_month = 'May'
        target_month_abv = 'May'
    elif (num_target_month == '06'):
        target_month = 'June'
        target_month_abv = 'Jun'
    elif (num_target_month == '07'):
        target_month = 'July'
        target_month_abv = 'Jul'
    elif (num_target_month == '08'):
        target_month = 'August'
        target_month_abv = 'Aug'
    elif (num_target_month == '09'):
        target_month = 'September'
        target_month_abv = 'Sep'
    elif (num_target_month == '10'):
        target_month = 'October'
        target_month_abv = 'Oct'    
    elif (num_target_month == '11'):
        target_month = 'Novemeber'
        target_month_abv = 'Nov'
    elif (num_target_month == '12'):
        target_month = 'Decemebr'
        target_month_abv = 'Dec'

    print(target_month + '-' + target_day + '-' + target_year)


    #year selector

    # for row in driver.find_elements_by_xpath(".//tr"):


    for ele in driver.find_elements_by_class_name('datepicker-days'):
        #if not  the target_year, go to the target_year
        if ele.find_element_by_class_name('switch').text != target_year:
            #ele.find_element_by_class_name('switch').click()
            driver.find_element_by_class_name('datepicker-days').find_element_by_class_name('switch').click()
            driver.implicitly_wait(2)
            driver.find_element_by_class_name('datepicker-months').find_element_by_class_name('switch').click()
            driver.implicitly_wait(2)
            #driver.find_element('2024').click()
            driver.find_element_by_xpath('//div[@class="datepicker-years"]/table/tbody/tr/td/span["' + target_year + '"]').click()
            print(driver.find_element_by_xpath('//div[@class="datepicker-years"]/table/tbody/tr/td/span["' + target_year + '"]'))
            #ele.find_element_by_class_name('switch').click()
            #/html/body/div[6]/div/div[3]/table/tbody/tr/td/span[2]
            for month in driver.find_elements_by_class_name('month'):
                print(month.text)
                if month.text == target_month_abv:
                    month.click()

                for day in ele.find_elements_by_class_name('day'):
                    print(day.text)
                    if day.text == target_day:
                        day.click()

        #if not the target_month, go to the target month
        if ele.find_element_by_class_name('switch').text != target_month:
            ele.find_element_by_class_name('switch').click()
            driver.implicitly_wait(2)
            for month in driver.find_elements_by_class_name('month'):
                print(month.text)
                if month.text == target_month_abv:
                    month.click()
                for day in ele.find_elements_by_class_name('day'):
                    print(day.text)
                    if day.text == target_day:
                        day.click()                    


        #if not the target_day, go to the target_day
        if ele.find_element_by_class_name('day active today').text != target_day:
            driver.implicitly_wait(2)
            for day in ele.find_elements_by_class_name('day'):
                print(day.text)
                if day.text == target_day:
                    day.click()
    # print(driver.find_elements_by_class_name('datepicker-days'))

    client_name_box = driver.find_element_by_id('select2-client_name-container')
    client_name_box.click()
    client_name_input = driver.find_element_by_class_name('select2-search__field')
    client_name_input.click()



    time.sleep(2)
    client_name_input.send_keys(client_name) #Column A
    time.sleep(5)
    client_name_input.send_keys(Keys.ENTER)


    # split_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div/section/div/form/div[5]/div/div/label/span[2]')
    # split_button.click()

    writting_agent_box = driver.find_element_by_id('select2-writing_agent-container')
    writting_agent_box.click()
    time.sleep(2)

    writting_agent_input = driver.find_element_by_class_name('select2-search__field')
    writting_agent_input.send_keys(agents) #B read before the "+"
    #<input class="select2-search__field" type="search" tabindex="0" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" role="textbox">
    time.sleep(5)
    writting_agent_input.send_keys(Keys.ENTER)

    # split_agent_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div/section/div/form/div[7]/div[2]/span/span[1]/span/span[1]/span')
    # split_agent_box.click()

    #if there is a split agent, run this code
    # split_agent_input = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
    # split_agent_input.send_keys('Lucy Matsumoto') #B read after the "+"
    # time.sleep(5)
    # split_agent_input.send_keys(Keys.ENTER)

    #if there is a trainee, run this code
    # trainee_no = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div/section/div/form/div[8]/div/label[2]')
    trainee_no = driver.find_element_by_xpath("//label[@for='trainee_no']")
    trainee_no.click()
    trainee_yes = driver.find_element_by_xpath("//label[@for='trainee_yes']")

    trainee_yes.click()
    # trainee_yes = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div/section/div/form/div[8]/div/label[1]')

    #trainee text box
    # trainee_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div/section/div/form/div[9]/div/span/span[1]/span/span[1]')
    # trainee_box.click()


    # trainee_box_input = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
    # trainee_box_input.send_keys()

    # Product Name
    product_name_box = driver.find_element_by_id('product_text')
    product_name_box.click()
    product_name_box.send_keys(product_name)
    product_name_box.send_keys(Keys.ENTER)


    #Policy #
    # policy_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div/section/div/form/div[10]/div/input')
    policy_box = driver.find_element_by_id('policy')
    policy_box.click()
    policy_box.send_keys(policy_number) #J
    policy_box.send_keys(Keys.ENTER)

    #Commented because there is not a need for AIR
    #AIR
    # air_no_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div/section/div/form/div[10]/div/label[2]')
    # air_yes_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div/section/div/form/div[10]/div/label[1]')

    #Total Points
    # total_points_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div/section/div/form/div[12]/div/input')
    total_points_box = driver.find_element_by_id('actualpointval')
    total_points_box.click()
    total_points_box.send_keys(total_points) #D

    #Notes
    notes_box = driver.find_element_by_id('notes_value')
    notes_box.send_keys(notes) #R

    #Pending Submission Switch
    pending_switch = driver.find_element_by_xpath("//label[@for='pending_switch']")
    pending_switch.click()


    #Uncomment when ready to add

    #Create a check and use a new column to activate this

    #add_to_tracker_button = driver.find_element_by_id('prod_btn')
    #add_to_tracker_button.click()

    return