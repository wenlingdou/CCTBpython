# 1. Using Selenium WebDriver, open the web browser.
#
# 2. Maximize the browser window.
#
# 3. Navigate to the 'https://www.canadianctb.ca/' website and check that this page has 'CCTB | Canadian College of Technology and Business' in the title and https://www.canadianctb.ca/Links to an external site. as the current URL.
#
# 4. Next, click by Virtual Student Lounge link text and navigate there.
#
# 5. Display current URL and title. Compare with your expected values. Use user-friendly messages.

import datetime
from selenium import webdriver   # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

app = 'CCTB'
cctb_url = 'https://www.canadianctb.ca/'
cctb_homepage_title = 'CCTB | Canadian College of Technology and Business'
cctb_virtual_url = 'https://www.canadianctb.ca/virtual-student-lounge'
cctb_virtual_title = 'Virtual Student Lounge | CCTB'

def setUp():
    print(f'Launch {app} App')
    print(f'--------------------------------------------------')

    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(cctb_url)
    if driver.current_url == cctb_url and driver.title == cctb_homepage_title:
        print(f'Welcome to {app}! {app} App website launched successfully!')
        print(f'{app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Homepage title: {driver.title}')
        tearDown()

def tearDown():
    if driver is not None:
        print('--------------------------------------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()

def virtual_st_lounge():
    if driver.current_url == cctb_url:
        driver.find_element(By.LINK_TEXT, 'Virtual Student Lounge').click()
        if driver.current_url == cctb_virtual_url and driver.title == cctb_virtual_title:
            # assert driver.current_url == cctb_virtual_url
            # assert driver.title == cctb_virtual_title
            print(f'{app} Virtual Student Lounge page URL: {cctb_virtual_url}, page title: {cctb_virtual_title}')
            print(f'{app} Virtual Student Lounge page is displayed successfully!')
            sleep(0.25)
        else:
            print(f'Virtual Student Lounge page is not displayed. Please check your code.')


setUp()
virtual_st_lounge()
tearDown()

