
import random
import requests
from bs4 import BeautifulSoup
import os

def card():
    #Card#
    response = requests.get("https://randomus.ru/name?type=101&sex=10&count=1") 
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find("span", class_="tag tag_result has-text-weight-bold has-background-white-bis is-size-4 is-size-5-mobile is-size-3-widescreen")
    ######
    #data#
    
    meciatch = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    day = random.randint(1, 31)

    file_card = open('data.txt', 'w+')
    file_card.write(f'''
    number_card = "{random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}"
    validity = "{random.randint(1, 12)}/{random.randint(22, 30)}"
    name = "{table.text}"
    cvv = "{random.randint(000, 999)}"
    ###########
    age = {random.choice(meciatch)} {day} {random.randint(1970, 2013)}
    ''')
    