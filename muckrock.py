#!/usr/bin/python2.7

import requests
import json
import time
import selenium
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

login_url = "https://www.muckrock.com/accounts/login/"

driver.get(login_url)

time.sleep(10)

all_urls = []

pages = {}

for url in open('muckrock.agencies').readlines():
    url = url.strip()
    driver.get(url) 
    page_source =  driver.page_source

    pages[url] = page_source

    time.sleep(1)

sys.exit(0)

for i in range(1,249):
    url = 'https://www.muckrock.com/agency/?page=%s' %  i
    driver.get(url)

    page_urls = driver.execute_script("""
        agencies = document.getElementsByTagName("table")[0].getElementsByTagName("tr")
        ret = []
        for ( i = 1 ; i < agencies.length ; i++ ) {
            ret.push(agencies[i].getElementsByTagName('td')[0].childNodes[0].href)
        }
        return ret
    """)

    all_urls += page_urls
    

for i in all_urls:
    print i 
