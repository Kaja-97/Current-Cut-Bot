#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
import os
import time



while (True):

    path="chromedriver.exe"
    options=webdriver.ChromeOptions()
    options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-sh-usage")




    driver =webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    url='https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule'
    pag=driver.get('https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule')
    pagg=driver.page_source


    soup=BeautifulSoup(pagg,'html.parser')
    soup1=soup.find('div',class_="fc-scroller fc-time-grid-container")

    from bs4 import BeautifulSoup


    #soup1=BeautifulSoup(ss,'html.parser')
    a=soup1.find_all('a')
    Time=[]
    Zone=[]

    for a in a:
        time=a.find('div',class_='fc-time').text
        Time.append(time)
        zone=a.find('span',class_='badge border border-light text-light fw-500').getText()
        Zone.append(zone)


    dic={'Zone':Zone,'Time':Time}
    table=pd.DataFrame(dic)
    tt=table[table['Zone']=='W']
    # msg=list(tt.iloc[0])

    #  Whatsapp sending #####################################
    # tim=pd.to_datetime(msg[1])
    # zon=msg[0]
    # text={zon:tim}
    # print(text)
    # print(str(table[table['Zone']=='W']).split()[-2:])
    # features="html.parser


    # Telegram sending ##########################################

    base_url='https://api.telegram.org/bot1938707924:AAHknoxOQa0hTqDhOY5jD5pX-bpbY5QdHwo/sendMessage'
    parameters={
        'chat_id':'-690438830',
        'text':str(tt)
    }

    res=requests.get(base_url,data=parameters)
    time.sleep(30)


# In[ ]:




