import requests
from bs4 import BeautifulSoup
import smtplib
import time

URl= 
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


def check_price:

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle")

    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[0:9])

    if(converted_price < your_price):
        send_mail()

def send_mail():
    server = smptlib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your gmail', 'your password')

    subject = 'price fell down'
    body = URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('from', 'to', msg)

    print('Email Has been sent to yo')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)