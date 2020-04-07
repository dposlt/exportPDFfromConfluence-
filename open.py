from selenium import webdriver
import time
from datetime import datetime

driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

texts = ['Předpisy - Přehled podle působnosti','Předpisy - Report revizí']

start_time = datetime.now().time().strftime('%H:%M:%S')
print(f'start: {start_time}')
if driver:
    driver.get('https://confluence-preprod.moneta.cz/collector/pages.action?key=MP')

    for link in texts:
        links = driver.find_element_by_link_text(link)
        links.click()

        menu = driver.find_element_by_id('action-menu-link')
        menu.click()

        export = driver.find_element_by_link_text('Export to PDF')
        export.click()
        print(f'{link} > saved to downloads')
        stop_time = datetime.now().time().strftime('%H:%M:%S')
        print(f'Stop download {link} - {stop_time}')
        time.sleep(2)

    print('alltime : {all}'.format(all = (datetime.strptime(stop_time,'%H:%M:%S') - datetime.strptime(start_time,'%H:%M:%S'))))
    time.sleep(5)

    driver.close()
else:
    print('driver not found')