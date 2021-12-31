from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

#Use only when you are on the url "https://bscpro.com/prospects_new"

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

def add_prospect(driver, clientInfo):
    #Start the add menu
        add_new_button = driver.find_element_by_class_name('w2ui-icon-plus')
        add_new_button.click()

        #Start filling the form
            #Title
                #chosen-single chosen-default
                #chosen-container chosen-container-single chosen-container-single-nosearch
                #Mr. Ms. Mrs. Dr. Rev.

        title_box = driver.find_element_by_class_name('chosen-container chosen-container-single chosen-container-single-nosearch')
        title_box.click()

        if(clientInfo[0] == 'Mr.'):
            mr_title = driver.find_element_by_xpath("//label[@for='Mr.']")
            mr_title.click()

        elif(clientInfo[0] == 'Ms.'):
            ms_title = driver.find_element_by_xpath("//label[@for='Ms.']")
            ms_title.click()

        elif(clientInfo[0] == 'Mrs.'):
            mrs_title = driver.find_element_by_xpath("//label[@for='Mrs.']")
            mrs_title.click()

        elif(clientInfo[0] == 'Dr.'):
            dr_title = driver.find_element_by_xpath("//label[@for='Dr.']")
            dr_title.click()

        elif(clientInfo[0] == 'Rev.'):
            rev_title = driver.find_element_by_xpath("//label[@for='Rev.']")
            rev_title.click()

        #Name
        name = clientInfo['First Name'] + ' ' + clientInfo['Last Name']
        name_box = driver.find_element_by_class_name('form-control name_input')
        name_box.click()
        name_box.send_keys(name)

        #Email
        email_box = driver.find_element_by_id('email')
        email_box.click(clientInfo['Email'])

        #Phone
        phone_box = driver.find_element_by_id('phone')
        phone_home_box = driver.find_element_by_id('phone_home')
        phone_office_box = driver.find_element_by_id('phone_office')

        phone_box.click(clientInfo['Phone Number'])
        phone_home_box.click(clientInfo['Home Number'])
        phone_office_box.click(clientInfo['Office Number'])

        #address
        address_box = driver.find_element_by_id('autocomplete')
        address_box.click()
        #leave blank
        address_box.send_keys()
 

        #How do you know her/him?
        question1_box = driver.find_element_by_id('que1')
        question1_box.click()
        question1_box.send_keys()

        #Occupation?
        question2_box = driver.find_element_by_id('que2')
        question2_box.click()

        #What have you told this person about our company so far?
        question3_box = driver.find_element_by_id('que3')
        question3_box.click()

            #Call Type
                #name="tag[]"
                #class="form-control tag select2-hidden-accessible"

                #value="250" BPM Invite
                #value="251" Help
                #value="252" 1 on 1 /BMP
                #value="253" FNA
                #value="254" KTP
                #value="255" Fast Start

            #Tags
                #name = "prospect_tag[]"
                #select2-serach__field
        call_type_box = driver.find_element_by_name('tag[]')
        call_type_box.click()

                #menu
        call_type_bpm_invite = driver.find_element_by_xpath("//label[@for='BPM Invite']")
        call_type_help = driver.find_element_by_xpath("//label[@for='Help']")
        call_type_1_on_1 = driver.find_element_by_xpath("//label[@for='1 on 1 /BMP]")
        call_type_fna = driver.find_element_by_xpath("//label[@for='FNA']")
        call_type_ktp = driver.find_element_by_xpath("//label[@for='KTP']")
        call_type_fast_start = driver.find_element_by_xpath("//label[@for='Fast Start']")

        if(clientInfo[0] == '1' or clientInfo == 'Yes'):
            call_type_bpm_invite.click()

        if(clientInfo[0] == '1' or clientInfo == 'Yes'):
            call_type_help.click()

        if(clientInfo[0] == '1' or clientInfo == 'Yes'):
            call_type_1_on_1.click()

        if(clientInfo[0] == '1' or clientInfo == 'Yes'):
            call_type_fna.click()

        if(clientInfo[0] == '1' or clientInfo == 'Yes'):
            call_type_ktp.click()

        if(clientInfo[0] == '1' or clientInfo == 'Yes'):
            call_type_fast_start.click()


            #3 Good Qualities
                #name = "quality1"
                #name = "quality2"
                #name = "quality3"

        quality1_box = driver.find_element_by_name('quality1')
        quality2_box = driver.find_element_by_name('quality2')
        quality3_box = driver.find_element_by_name('quality3')

        if clientInfo[0]:
            quality1_box.click()
            quality1_box.send_keys(clientInfo['Quality1'])

        if clientInfo[0]:
            quality2_box.click()
            quality2_box.send_keys(clientInfo['Quality2'])
            #send keys

        if clientInfo[0]:
            quality3_box.click()
            quality3_box.send_keys(clientInfo['Quality3'])
            #send keys

            #Spouse Name
                #name = "spouse_name"
                #value id = "spouse_name"

        spouse_box = driver.find_element_by_name('spouse_name')
        
        if clientInfo[0]:
            spouse_box.click()
            spouse_box.send_keys(clientInfo['Spouse'])
        

        #profile
            #1 25 yo +
        year25_box = driver.find_element_by_id('editprofile_125')
        if (clientInfo[0] == 1 or clientInfo == 'Yes'):
            year25_box.click()

            #2 Married1
        married_box = driver.find_element_by_id('editprofile_126')
        if (clientInfo[0] == 1 or clientInfo == 'Yes'):
            married_box.click()

            #3 Dependent Children  
        dep_child_box = driver.find_element_by_id('editprofile_127')
        if (clientInfo[0] == 1 or clientInfo == 'Yes'):
            dep_child_box.click()  

            #4 Homeowner    
        homeowner_box = driver.find_element_by_id('editprofile_128')
        if (clientInfo[0] == 1 or clientInfo == 'Yes'):
            homeowner_box.click() 

            #5 Solid Career Background
        solid_career_box = driver.find_element_by_id('editprofile_129')
        if (clientInfo[0] == 1 or clientInfo == 'Yes'):
            solid_career_box.click()   

            #6 $40000+ Income
        income_40k_box = driver.find_element_by_id('editprofile_130')
        if (clientInfo[0] == 1 or clientInfo == 'Yes'):
            income_40k_box.click()    

            #7 Dissatisfied
        dissatisfied_box = driver.find_element_by_id('editprofile_131')
        if (clientInfo[0] == 1 or clientInfo == 'Yes'):
            dissatisfied_box.click() 

            #8 Entreprenuerial  
        entreprenuerial_box = driver.find_element_by_id('editprofile_132')
        if (clientInfo[0] == 1 or clientInfo == 'Yes'):
            entreprenuerial_box.click()         
            #9 Span
                
        span_box = driver.find_element_by_id('editprofile_133')
        if (clientInfo[0] == 1 or clientInfo == 'Yes'):
            span_box.click() 

        #Contact Type
        contact_type_box = driver.find_element_by_class_name('chosen-container chosen-container-single chosen-container-single-nosearch')
        contact_type_box.click()
        
            # for element in driver.find_elements_by_class_name('hosen-container chosen-container-single chosen-container-single-nosearch chosen-container-active chosen-with-drop'):
            #     if (element == 'Friend'):
                #class="chosen-results"
            
                #Friend
                #class="active-result" style data-option-array-index="0"
        if (clientInfo[0] == 'Friend' or clientInfo[0] == 'friend'):
            friend_option = driver.find_element_by_xpath("//label[@for='Friend']")
                #Acquaintance
                #class="active-result" style data-option-array-index="1"
        if (clientInfo[0] == 'Acquaintance' or clientInfo[0] == 'acquaintance'):
            friend_option = driver.find_element_by_xpath("//label[@for='Acquaintance']")                
                #Prospected
                #class="active-result" style data-option-array-index="2"
        if (clientInfo[0] == 'Prospected' or clientInfo[0] == 'prospected'):
            friend_option = driver.find_element_by_xpath("//label[@for='Prospected']")    
                #Family
                #class="active-result" style data-option-array-index="3"
        if (clientInfo[0] == 'Family' or clientInfo[0] == 'family'):
            friend_option = driver.find_element_by_xpath("//label[@for='Family']")                  
                #Referred By
                #class="active-result" style data-option-array-index="4"
        if (clientInfo[0] == 'Referred By' or clientInfo[0] == 'referred by'):
            friend_option = driver.find_element_by_xpath("//label[@for='Referred By']")   

        #Notes
        notes_box = driver.find_element_by_id('note_txt')
        notes_box.click()

        #Birthday
        birthday_box = driver.find_element_by_name('birthday')
        birthday_box.click()

        #Anniversary
        anniversary_box = driver.find_element_by_name('anniversary')
        anniversary_box.click()

        #Start Date
        recruit_start_date_box = driver.find_element_by_name('recuit_start_date')
        recruit_start_date_box.click()
            
        #Recruiter
        recruiter_box = driver.find_element_by_id('select2-recruiter-container')
        recruiter_box.click()

        #Pipeline Estimate
        pipeline_est_box = driver.find_element_by_name('pipeline_amount')
        pipeline_est_box.click()


        #Assigned To
            #class="select2-selection__placeholder" >Select Assign To<
            #id="select2-assigned_to-container"
                #drop down menu search box
                #class="select2-search__field"

        assigned_to_box = driver.find_element_by_id('select2-assigned_to-container')
        assigned_to_box.click()

        select2_search_box = driver.find_element_by_class_name('select2-search__field')
        select2_search_box.click()
        select2_search_box.send_keys()

        #Team Leader
            #id="select2-team_leader-container"
                #drop down menu search box
                #class="select2-search__field"

        team_leader_box = driver.find_element_by_id('select2-team_leader-container')
        team_leader_box.click()
        team_leader_input_box = driver.find_element_by_class_name('select2-search__field')
        team_leader_input_box.click()
        
        #Save Button
            
#should pass the prospect id or clientInfo as a parameter                    
def edit_prospect(driver, clientInfo):

    #class = mm-page
        #id = wrap
            #class = row
                #id = content, class = col-md-12 fullscreen
                    #id = grid_grid_records, class = w2ui-grid-records
                    #iterate through tr id = grid_grid_rec_*
    
    #client_name = clientInfo['f']
    client_name = clientInfo['First Name'] + ' ' + clientInfo['Last Name']

    title_string = "//div[@title='{client_name}']"
    #record = driver.find_element_by_xpath(title_string)
    
    #name_string = clientInfo['']

    record = driver.find_element_by_xpath("{title_string}")

    actionChains = ActionChains(driver)
    actionChains.double_click(record).perform()

