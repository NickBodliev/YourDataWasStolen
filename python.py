import requests
import cloudscraper

scraper = cloudscraper.create_scraper()  #module to bypass Cloudflare's anti-bot page (also known as "I'm Under Attack Mode", or IUAM)

url = 'https://haveibeenpwned.com/unifiedsearch/'

print("533 million Facebook users' phone numbers and email addresses have been leaked online! Checke if yours are sefe!")

mail = input("Input the mail/phone number you want to check:")
formatedMail = mail.replace('@','%40')
url = url + formatedMail
r = scraper.get(url)
if r.status_code == 404:
    print("Your data is safe")
else:
    print("Your data was stolen!")
