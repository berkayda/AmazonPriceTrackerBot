import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com.tr/Viko-Yonca-Toprakl%C4%B1-Priz-Siyah/dp/B07BK7T1B6/ref=zg-bs_home-improvement_sccl_2/257-6051429-8242144?pd_rd_w=PAYnh&content-id=amzn1.sym.81881d61-dcb9-463e-95e4-e45e6f4362b9&pf_rd_p=81881d61-dcb9-463e-95e4-e45e6f4362b9&pf_rd_r=K500CTD0MG6YZZNZYRXC&pd_rd_wg=1Qv4M&pd_rd_r=fc118af7-d080-414b-8cc1-7fd1a6f58d19&pd_rd_i=B07BK7T1B6&psc=1'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

def price_check(URL, max_price):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").getText().strip()

    price = soup.find(id="priceblock_ourprice").getText().strip()

    new_price = float(price[1:-1].replace(",","."))

    print(new_price)

    if(new_price >= max_price):
        send_email("RECEIVER MAIL ADDRESS",URL) #DO NOT FORGET TO WRITE YOUR MAIL ADDRESS
    else:
        print("Urun fiyati dustu.")


def send_email(toMail, url):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("SENDER MAIL ADDRESS","PASSWORD") #DO NOT FORGET TO WRITE YOUR MAIL ADDRESS & PASSWORD


    subject = 'Fiyat Artti!'

    body = 'Urun Linki: ' + url

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        "SENDER MAIL ADDRESS", #DO NOT FORGET TO WRITE YOUR MAIL ADDRESS
        "RECEIVER MAIL ADDRESS", #DO NOT FORGET TO WRITE YOUR MAIL ADDRESS
        msg
    )
    print("mesaj gonderildi")
    server.quit()

while(True):
    price_check(URL,100)
    time.sleep(6)