#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
from bs4 import BeautifulSoup
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_argument('headless')
opts.add_argument('no-sandbox')
browser = webdriver.Chrome(options=opts)
browser.get('https://classes.usc.edu/term-20191/#')
# browser.find_element_by_css_selector('a[data-sort-by="data-title"]').click()
soup = BeautifulSoup(browser.page_source, "html.parser")
programs = soup.select('li[data-type="department"] a')
for program in programs:
    #time.sleep(5)
    browser.get(program['href'])
    soup = BeautifulSoup(browser.page_source, "html.parser")
    sessions = soup.select('tr[data-section-id]')
    for session in sessions:
        current = {}
        current['section'] = session.find(class_='section').get_text()
        current['type'] = session.find(class_='type').get_text()
        current['time'] = session.find(class_='time').get_text()
        current['days'] = session.find(class_='days').get_text()
        current['instructor'] = session.find(class_='instructor').get_text()
        print('"'+current['section']+'", "'+current['type']+'", "' +
              current['time']+'", "'+current['days']+'", "'+current['instructor']+'"')
