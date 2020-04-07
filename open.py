from selenium import webdriver
import time, logfile
from datetime import datetime

driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

texts = ['https://confluence-preprod.moneta.cz/x/qwUhSw','https://confluence-preprod.moneta.cz/x/ZgQhSw','https://confluence-preprod.moneta.cz/x/IQEhSw']

start_time = datetime.now().time().strftime('%H:%M:%S')
logfile.loggin(start_time)
if driver:
    driver.get('https://confluence-preprod.moneta.cz/collector/pages.action?key=MP')

    for link in texts:
        links = driver.get(link)
        #links.click()

        menu = driver.find_element_by_id('action-menu-link')
        menu.click()

        export = driver.find_element_by_link_text('Export to PDF')
        export.click()
        print(f'{link} > saved to downloads')
        stop_time = datetime.now().time().strftime('%H:%M:%S')
        logfile.loggin(f'{link} > {stop_time}')
        time.sleep(2)

    allTime = datetime.strptime(stop_time,'%H:%M:%S') - datetime.strptime(start_time,'%H:%M:%S')
    #print('alltime : {all}'.format(all = allTime))
    logfile.loggin(f'celkove: {allTime}')
    time.sleep(5)

    driver.close()
else:
    print('driver not found')