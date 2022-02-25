import urllib.request as req

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re

options = Options()
options.add_argument("--disable-notifications")
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://zh-tw.facebook.com/AKB48TeamTP")
time.sleep(3)

for x in range(1, 2):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

my_selector = '.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gpro0wi8.oo9gr5id.lrazzd5p'
see_more = chrome.find_elements(By.CSS_SELECTOR, my_selector)
print(len(see_more))
print(type(see_more[0]))

scripts = "\
var elements = document.getElementsByClassName('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p');\
for(let i=0;i < elements.length;i++){\
    if(elements[i].innerHTML=='顯示更多'){\
        console.log(elements[i].innerHTML);\
        elements[i].click();\
    }\
}"

chrome.execute_script(scripts)
time.sleep(1)

import bs4
root = bs4.BeautifulSoup(chrome.page_source, "html.parser")
str1 = 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m'
targets = root.find_all('span',{'class':str1})

for target in targets:
    posts = target.find_all('div', {'dir': 'auto'})
    isLive = 0;
    
    for post in posts:
        if post.getText().startswith("#浪Live"):
            isLive = 1;
    if isLive == 1:
        print("==============================")
    date_text = ""
    for post in posts:
        if isLive == 1:
            tmp_text = post.getText()
            if '月' in tmp_text and '日' in tmp_text:
                date_text = tmp_text
            if post.getText().startswith('林于馨'):
                print(date_text)
                print(post.getText())
                date_text = ""

chrome.quit()
