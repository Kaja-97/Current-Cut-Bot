#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
import os
import time
import chromedriver_binary
import telebot





path="chromedriver.exe"
options=webdriver.ChromeOptions()
options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-sh-usage")

bot = telebot.TeleBot('1938707924:AAHknoxOQa0hTqDhOY5jD5pX-bpbY5QdHwo')


########### telegram bot'''#########################################
@bot.message_handler(commands=['W'])
def greet(message):
    bot.reply_to(message, mmm)
    

########### telegram bot'''#########################################
driver =webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
url='https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule'
pag=driver.get('https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule')
pagg=driver.page_source


soup=BeautifulSoup(pagg,'html.parser')
soup1=soup.find('div',class_="fc-scroller fc-time-grid-container")





gg=soup1.find_all('a')
Time=[]
Zone=[]

for a in gg:
    time=a.find('div',class_='fc-time').text
    Time.append(time)
    zone=a.find('span',class_='badge border border-light text-light fw-500').getText()
    Zone.append(zone)

dic = {'Zone': Zone, 'Time': Time}
table = pd.DataFrame(dic)
tt = table[table['Zone'] == 'W']
mmm = str(tt)

bot.polling()





