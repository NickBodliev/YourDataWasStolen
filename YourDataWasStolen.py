import requests
import cloudscraper
import re

notMailChars = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
url = 'https://haveibeenpwned.com/unifiedsearch/'

def check(str):                     #check if the passed string is an email (not contains forbiden signs)
    if re.search(notMailChars, str):    
        return True                 
    else:
        return False
        
scraper = cloudscraper.create_scraper()  #module to bypass Cloudflare's anti-bot page (also known as "I'm Under Attack Mode", or IUAM)

print("533 million Facebook users' phone numbers and email addresses have been leaked online! Checke if yours are sefe!")

data = input("Input the mail/phone number you want to check:")

#check of the format of the written data
while not ("+" in data or "@" in data): #control if written data hasn't any @ sign (for email addresses) or + sign (for phone numbers)                    
    if data.lower().islower():                      #if this condition is true, the input data contains letters, so it's an email address
        data = input("Invalid email! Try again:")
    else:                                           #else it's a phone number 
        data = input("Invalid phone number! Try again:")

formatedData = data.replace('@','%40')
url = url + formatedData
r = scraper.get(url)
if r.status_code == 404:
    print("Your data is safe")
else:
    print("Your data was stolen!")