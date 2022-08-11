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
from telebot import types
from dotenv import load_dotenv
import selenium 
import datetime


config = load_dotenv(".env")


API_KEY=os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


########### telegram bot'''#########################################

@bot.message_handler()
def scrap(msg):
    zz=str(msg.text)
    scraper(zz)
    for i in A:
        bot.reply_to(msg,i)
    
@bot.message_handler(commands=['start'])
def greet(message):
#     user_first_name = str(message.chat.first_name) 
    bot.reply_to(message, f"Hey!  \n Welcome 😍 \n,Please type your zone , (ex :- /A )  ")
    
########### telegram bot'''#########################################
def scraper(x):
    #######################################################################################
    path="chromedriver.exe"
    options=webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-sh-usage")
    ###############################################################hhhhhhhhh######################
    driver =webdriver.Chrome(executable_path=r"C:\Users\kajan\Desktop\Python\Web Scraping\chromedriver.exe",chrome_options=options)
    url='https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule'
    pag=driver.get('https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule')
    pagg=driver.page_source
    soup=BeautifulSoup(pagg,'html.parser')
    soup1=soup.find('div',class_="fc-scroller fc-time-grid-container")
    #soup1=BeautifulSoup(ss,'html.parser')
    a=soup1.find_all('a')
    global A
    if len(a)==0:
        A=['No Power Cut Today 🤔']
    else:

        Time=[]
        Zone=[]
        for a in a:
            time=a.find('div',class_='fc-time').text
            Time.append(time)
            zone=a.find('span',class_='badge border border-light text-light fw-500').getText()
            Zone.append(zone)
            print(Zone)
        dic={'Zone':Zone,'Time':Time}

        if x not in Zone:
            A='Please Type Correct Zone'
        else:
            table=pd.DataFrame(dic)
            AA=table[table['Zone']==x]
            code_html='*Title of the message*' 
            A=[]
            if AA.empty == False:
                for i in range(len(AA)):
                    B=code_html=code_html + '\n\n Zone:' + str((AA['Zone'].iloc[i])) +' - '+' Time: ' + str((AA['Time'].iloc[i]))
                    A.append(B)
                    print('XX')

bot.polling()
