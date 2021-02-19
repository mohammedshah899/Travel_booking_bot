import selenium
from selenium import webdriver
import time
import datetime
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup as soup

PATH = 'C:\Program Files (x86)\chromedriver.exe'

TEXT = 'Dubai'
date_entry = input('Enter a start date in YYYY-MM-DD format\n')
year, month, day = map(int, date_entry.split('-'))
start_date = datetime.datetime(year, month, day)
start_date.strftime('%B')


date_entry1 = input('Enter a end date in YYYY-MM-DD format\n')
year, month, day = map(int, date_entry1.split('-'))
#user_end_date = datetime.datetime(year, month, day)
end_date = datetime.datetime(year, month, day)

guests = input('Enter the no. of Guests\n')

driver = webdriver.Chrome(PATH)
driver.set_window_size(800, 657)




url = "https://www.trivago.ae/en?themeId=280&sem_keyword=trivago&sem_creativeid=222288966136&sem_matchtype=e&sem_network=g&sem_device=c&sem_placement=&sem_target=&sem_adposition=&sem_param1=&sem_param2=&sem_campaignid=281577075&sem_adgroupid=22877527395&sem_targetid=kwd-5593367084&sem_location=1000013&cip=9711900005&gclid=CjwKCAiA_eb-BRB2EiwAGBnXXjAwn2uzenHFevo-O6IehMWgx5YzWAUeZxmXgONZ8IHdpiAv0c_cRRoCCXQQAvD_BwE"

driver.get(url)

search = driver.find_element_by_id('querytext')
search.send_keys(TEXT)
time.sleep(2)
option = driver.find_element_by_class_name('ssg-suggestion__info')
option.click()

time.sleep(2)

DateWidget = driver.find_element_by_class_name('dealform-button__label')
headers = driver.find_elements_by_id('cal-heading-month')
print(headers[0])
first_header  = headers[0].text.split(' ')[0]

first_calender_body = driver.find_elements_by_tag_name('td')


while first_header != start_date.strftime('%B'):
        next_arrow = driver.find_element_by_class_name('cal-btn-next').click()
        first_header = headers[0].text.split(' ')[0]
        
for row in first_calender_body:
    if row.text == '':
        continue
    if(int(row.text) == start_date.day):
        row.click()
        break

while first_header != end_date.strftime('%B'):
        next_arrow = driver.find_element_by_class_name('cal-btn-next').click()
        first_header = headers[0].text.split(' ')[0]
        
for row in first_calender_body:
    if row.text == '':
        continue
    if(int(row.text) == end_date.day):
        row.click()
        break


time.sleep(2)

infoWidget = driver.find_element_by_tag_name('fieldset')
buttonWidget = driver.find_element_by_tag_name('ul')
apply = driver.find_element_by_xpath('//*[@id="js-fullscreen-hero"]/div[1]/form/div/div[4]/fieldset/ul/li[2]/button')
final_search = driver.find_element_by_xpath('//*[@id="js-fullscreen-hero"]/div[1]/form/div/button[2]')
if(int(guests) > 2):
        add = driver.find_element_by_id('adults-input')
        add.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        add.send_keys(guests)
        add.send_keys(Keys.RETURN)
        time.sleep(1)
        apply.click()
        time.sleep(1)
        final_search.click()


        
        




    


        

        



