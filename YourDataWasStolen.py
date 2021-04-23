import requests
import cloudscraper
import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

def check(email):
    if(re.search(regex, email)):
        
scraper = cloudscraper.create_scraper()  #module to bypass Cloudflare's anti-bot page (also known as "I'm Under Attack Mode", or IUAM)

url = 'https://haveibeenpwned.com/unifiedsearch/'

print("533 million Facebook users' phone numbers and email addresses have been leaked online! Checke if yours are sefe!")


data = input("Input the mail/phone number you want to check:")

"""
while not ("+" in data or "@" in data):
    if data.lower().islower():                  #mail
        input("Invalid email! Try again")
    else:                                   #phone number    
"""


formatedMail = data.replace('@','%40')
url = url + formatedMail
r = scraper.get(url)
if r.status_code == 404:
    print("Your data is safe")
else:
    print("Your data was stolen!")
