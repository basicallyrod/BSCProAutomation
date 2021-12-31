import os
#from dotenv import load_dotenv
import numpy as np
import pandas as pd
import datetime
import json
import schedule
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from BSC.production_tracker.add_production import add_production as prod_helper
from BSC.prospect_tracker.prospect_tracker import edit_prospect
from SpreadsheetDictionary import spreadsheet_id_dictionary, range_id_dictionary, person_id_dictionary, SCOPES, SCRIPT_ID, RECIPIENT
from GoogleWorkspace.fetch_sheet import sheet_data
#from GoogleWorkspace.update_detector import looks_for_changes

from BSC import navigation_manager

from GoogleWorkspace.scriptHandler import scriptExecute

from httplib2 import Http


PATH = "/usr/bin/chromedriver"
#driver = webdriver.Chrome(PATH)

#Reminds the person of the client's info
def AnniversaryReminder(driver):
    today = datetime.date.today().strftime("%m/%d")

    #Looks through all the the spreadsheets
    for i_index in range(len(spreadsheet_id_dictionary)):

        #grabs data
        value = sheet_data(spreadsheet_id_dictionary[i_index],range_id_dictionary[0])
        values = pd.DataFrame(value)

        #set up the header_row
        header_row = 0
        values.columns = values.iloc[header_row]
        values = values.drop(header_row)
        values = values.reset_index(drop=True)

        #set up time/dates to compare
        dates = pd.to_datetime(values['Inception Date'], infer_datetime_format=True)        #results = dates.dt.strftime("%m/%d")
        results = dates.dt.strftime("%m/%d")

        #Use i+1 for other people besides 0(dev's email)
        recipient = RECIPIENT[0]
        script_id = SCRIPT_ID[0]

        #Looks through each row in the spreadsheet
        for j_index in range(len(results)):

            #Runs a email script if it is today.
            if(results[j_index] == today):
                clientInfo = pd.DataFrame.to_json(values.loc[j_index])
                
                #print(f'{j_index} row is running!')
                #scriptExecute(script_id, recipient, clientInfo)       
            else:
                print('no')

        spreadsheet_filename = f'./GoogleWorkspace/{person_id_dictionary[i_index]}_spreadsheet.csv'
        pd.DataFrame(values).to_csv(spreadsheet_filename)
            
def detect_changes(csv1, csv2):
    #if pd.DataFrame(csv1).compare(csv2).any() == True:
    # csv1['Month'].infer_objects().dtypes
    # csv2['Month'].infer_objects().dtypes
    # csv1['Month'].convert_dtypes(infer_objects=True, convert_string=False, convert_integer=True, convert_boolean=True, convert_floating=False)
    # csv2['Month'].convert_dtypes(infer_objects=True, convert_string=False, convert_integer=True, convert_boolean=True, convert_floating=False)
    csv1['Month'] = pd.to_numeric(csv1['Month'])
    csv2['Month'] = pd.to_numeric(csv2['Month'])
    # print(csv1['Month'].dtype)
    # print(csv2['Month'].dtype)
    # print(csv1['Month'])
    # print(csv2['Month'])
    print(csv1.compare(csv2))

    # df = pd.DataFrame(
    #     {
    #         "col1": ["a", "a", "b", "b", "a"],
    #         "col2": [1.0, 2.0, 3.0, np.nan, 5.0],
    #         "col3": [1.0, 2.0, 3.0, 4.0, 5.0]
    #     },
    #     columns=["col1", "col2", "col3"],
    # ) 
    # df2 = df.copy()
    # df2.loc[0, 'col1'] = 'c'
    # df2.loc[2, 'col3'] = 4.0

    # print(df.compare(df2))

    # print(csv1.dtypes)
    # print(csv2.dtypes)
    if csv1.equals(csv2):
        #if there are differences, update the bsc_prospect page
        print('true')
        return True
        pass
    else:
        print('false')
        pass

def main():
    i = 0

    #if there is a change in the spreadsheet, 
    #login to bsc and adjust for the changes

    #test version, logs in, goes to Prospect Tracker and look for the prospect
    # if (i == 0):
    #     #logs into BSC Pro
    #     navigation_manager.init_login(driver)

    #     #navigates to the Prospect Tracker page
    #     navigation_manager.prospect_tracker(driver)

    #     #Tries to look for Judith Jones in the test version
    #     #
    #     driver.implicitly_wait(5)
    #     edit_prospect(driver)
        

    #else, 
    #print(f'iteration: {i}')
    #AnniversaryReminder(driver)


    spreadsheet_filename = f'./GoogleWorkspace/{person_id_dictionary[1]}_spreadsheet.csv'
    value1 = pd.read_csv(spreadsheet_filename)

    #grabs data
    #value = sheet_data(spreadsheet_id_dictionary[i_index],range_id_dictionary[0])
    df1 = pd.DataFrame(value1)

    #set up the header_row
    header_row = 0
    #values1.columns = values1.iloc[header_row]
    #values1 = values1.drop(header_row)
    df1 = df1.drop(columns = df1.columns[0])
    df1 = df1.reset_index(drop=True)

    #pd_csv1 = values1.to_csv('pd_csv1.csv')
    df1 = pd.DataFrame(df1)
    #pd.DataFrame(pd_csv1).to_csv('pd_csv1.csv')

    #gets current/updated data
    value2= sheet_data(spreadsheet_id_dictionary[1],range_id_dictionary[0])

    #value2 = f'./GoogleWorkspace/{person_id_dictionary[1]}_spreadsheet.csv'
    df2 = pd.DataFrame(value2)
    
    df2 = df2.reset_index(drop=True)
    df2.columns = df2.iloc[header_row]
    #df2 = df2.drop(axis = 1)
    #df2.columns = 'test'
    #df2.columns[0] = r''
    df2 = df2.drop(header_row)
    #df2 = df2.drop(0, axis=1)
    
    df2 = df2.replace(r'^\s*$', np.nan, regex=True)
    df2 = df2.fillna(value=np.nan)
    
    df2 = df2.reset_index(drop=True)
    #df2 = df2.rename_axis(index=None)
    df2.columns.name = None
    #df2 = df2.drop(df2.columns[0], axis=1)

    #df2.columns = '0'
    #df2 = df2.drop(0, axis = 'columns')

    # print(df1)
    # print(df2)
    detect_changes(df1, df2)
    

    i = i + 1


#run with main to test/dev
if __name__ == "__main__":
    main()

#Uncomment below to run as a background process

#schedule.every().day.at("14:00").do(main)

# while True:
#     schedule.run_pending()
#     time.sleep(60)