
#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
import os
import time
import telebot
import chromedriver_binary
from dotenv import load_dotenv
config = load_dotenv(".env")





path="chromedriver.exe"
options=webdriver.ChromeOptions()
options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-sh-usage")

API_KEY=os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

#############################################################################################
# @bot.message_handler(commands=['Paper'])
# def greet(message):
#     try:
#         today=datetime.datetime.now().strftime('%Y-%m-%d')
#         chat_id=message.chat.id
#         pagelist=[]
#         paperlist=[]
#         for i in range(1,11):
#             ur='https://epaper.virakesari.lk/newspaper/Daily/main/{}#page-{}'.format(today,i)
#             pagelist.append(ur)
#         for i,ii in enumerate(pagelist,start=1):
#             options=webdriver.ChromeOptions()
#             options.headless = True
#             driver =webdriver.Chrome(executable_path=r"C:\Users\kajan\Desktop\Python\Web Scraping\chromedriver",options=options)
#             driver.get(url=ii)
#             soup=BeautifulSoup(driver.page_source,'html')
#             paperpg=soup.find('img',id='pageImage')['src']
#             bot.send_photo(chat_id, paperpg, protect_content=True ,disable_notification=True)
#     except Exception:
#         bot.reply_to(message,'sorry , maintenance Break' )









########### telegram bot'''#########################################
@bot.message_handler(commands=['A'])
def greet(message):
    bot.reply_to(message,A )
    
    
@bot.message_handler(commands=['B'])
def greet(message):
    bot.reply_to(message,B )
    
    
@bot.message_handler(commands=['C'])
def greet(message):
    bot.reply_to(message,C )
   
    
@bot.message_handler(commands=['D'])
def greet(message):
    bot.reply_to(message,D )
 
    
@bot.message_handler(commands=['E'])
def greet(message):
    bot.reply_to(message,E )
    
    
@bot.message_handler(commands=['F'])
def greet(message):
    bot.reply_to(message,F )
   
    
@bot.message_handler(commands=['G'])
def greet(message):
    bot.reply_to(message,G )
    
    
@bot.message_handler(commands=['H'])
def greet(message):
    bot.reply_to(message,H )
  
    
@bot.message_handler(commands=['I'])
def greet(message):
    bot.reply_to(message,I )


@bot.message_handler(commands=['J'])
def greet(message):
    bot.reply_to(message,J )

@bot.message_handler(commands=['K'])
def greet(message):
    bot.reply_to(message,K )

@bot.message_handler(commands=['L'])
def greet(message):
    bot.reply_to(message,L )

@bot.message_handler(commands=['P'])
def greet(message):
    bot.reply_to(message,P )
    print(tt)
@bot.message_handler(commands=['Q'])
def greet(message):
    bot.reply_to(message,Q )

@bot.message_handler(commands=['R'])
def greet(message):
    bot.reply_to(message,R )

@bot.message_handler(commands=['S'])
def greet(message):
    bot.reply_to(message,S )
    
@bot.message_handler(commands=['T'])
def greet(message):
    bot.reply_to(message,T )

@bot.message_handler(commands=['U'])
def greet(message):
    bot.reply_to(message,U )

@bot.message_handler(commands=['V'])
def greet(message):
    bot.reply_to(message,V )

@bot.message_handler(commands=['W'])
def greet(message):
    bot.reply_to(message,W )
    
@bot.message_handler(commands=['I love you'])
def greet(message):
    bot.reply_to(message,'Me too ❤️' )
    
@bot.message_handler(commands=['start'])
def greet(message):
#     user_first_name = str(message.chat.first_name) 
    bot.reply_to(message, f"Hey!  \n Welcome 😍 \nPlease type your zone , (ex :- /A ) \n\n Type /Paper For newspaper  ")
    
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



dic={'Zone':Zone,'Time':Time}
table=pd.DataFrame(dic)


AA=table[table['Zone']=='A']
A=str(AA)

BB=table[table['Zone']=='B']
B=str(BB)

CC=table[table['Zone']=='C']
C=str(CC)

DD=table[table['Zone']=='D']
D=str(DD)

EE=table[table['Zone']=='E']
E=str(EE)

FF=table[table['Zone']=='F']
F=str(FF)

GG=table[table['Zone']=='G']
G=str(GG)

HH=table[table['Zone']=='H']
H=str(HH)

II=table[table['Zone']=='I']
I=str(II)

JJ=table[table['Zone']=='J']
J=str(JJ)

KK=table[table['Zone']=='K']
K=str(KK)

LL=table[table['Zone']=='LL']
L=str(LL)

PP=table[table['Zone']=='P']
P=str(PP)

QQ=table[table['Zone']=='Q']
Q=str(QQ)

RR=table[table['Zone']=='R']
R=str(RR)

SS=table[table['Zone']=='S']
S=str(SS)

TT=table[table['Zone']=='T']
T=str(TT)

UU=table[table['Zone']=='U']
U=str(UU)

VV=table[table['Zone']=='V']
v=str(VV)

WW=table[table['Zone']=='W']
W=str(WW)




bot.polling()





