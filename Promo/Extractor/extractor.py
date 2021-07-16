import re
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import time
import colorama
colorama.init()
googleUrl = 'https://www.google.com/search?q='
print(colorama.Fore.LIGHTGREEN_EX + "Enter your Keyword: ", end='')
inputVal = input("~ ")
newInputVal = inputVal.lower().rstrip().replace(" ", "+").replace(".", "").replace(":", "").replace(";", "").replace("&", "and")
starting_url = 'https://www.google.com/search?q='+newInputVal+"+email+"+"id"
unprocessed_urls = deque([starting_url])
processed_urls = set()
emails = set()
print(colorama.Fore.LIGHTRED_EX + "Enter the time till you want to run this program... [In minutes]: ", end='')
max_time = int(input('~ '))*60
start_time = time.time()
extractedEmails = []
while len(unprocessed_urls):
    if (time.time() - start_time) >= max_time:
        break
    url = unprocessed_urls.popleft()
    processed_urls.add(url)
    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url
    print(colorama.Fore.LIGHTYELLOW_EX+"Extracting from: %s" % url)
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    emails.update(new_emails)
    print(colorama.Fore.LIGHTWHITE_EX+"Extracted... \n")
    for i in emails:
            extractedEmails.append(i+"\n")
    soup = BeautifulSoup(response.text, 'lxml')
    for anchor in soup.find_all("a"):
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        if link.startswith('/'):
            link = base_url + link
        elif not link.startswith('http'):
            link = path + link
        if not link in unprocessed_urls and not link in processed_urls:
            unprocessed_urls.append(link)
print(colorama.Fore.LIGHTCYAN_EX+'Time is up... Removing bad emails')
file1 = open("C:\\Users\\anand59\\Desktop\\Promo\\Extractor\\Extract.txt","a+")
goodEmails = list(set(extractedEmails))
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(email):  
    if(re.search(regex,email)):  
        return True 
    else:  
        return False
veryGoodEmails=[]
for i in range (len(goodEmails)):
    if check(goodEmails[i])==True:
        veryGoodEmails+=goodEmails[i]
bad_words = ['nic', 'gov', 'sbi', 'bank', 'google', 'beauty', 'traders']
for line in veryGoodEmails:
    if not any(bad_word in line for bad_word in bad_words):
        file1.write(line)
file1.close() 

print(colorama.Fore.LIGHTWHITE_EX+'Done goodbye!')