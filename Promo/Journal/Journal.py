import re
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import colorama
colorama.init()

rf = open("C:\\Users\\anand59\\Desktop\\Promo\\Journal\\company.txt", 'r+')
unprocessed_urls = rf.readlines()

for i in range(len(unprocessed_urls)):
	unprocessed_urls[i]=unprocessed_urls[i][:-1]
	unprocessed_urls[i]='https://www.google.com/search?q='+unprocessed_urls[i].lower().rstrip().replace(" ", "+").replace(".", "").replace(":", "").replace(";", "").replace("&", "and")+"+email+"+"id"

unprocessed_urls = deque(unprocessed_urls)

processed_urls = set()

emails = set()

extractedEmails = []

while len(unprocessed_urls):
	if unprocessed_urls:
		url = unprocessed_urls.popleft()
		processed_urls.add(url)

		parts = urlsplit(url)
		base_url = "{0.scheme}://{0.netloc}".format(parts)
		path = url[:url.rfind('/')+1] if '/' in parts.path else url

		print(colorama.Fore.LIGHTGREEN_EX + "Finding emails from: %s" % url)
		try:
			response = requests.get(url)
		except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
			continue

		new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
		emails.update(new_emails)
		print(colorama.Fore.WHITE + 'Got emails of company')
		for i in emails:
			extractedEmails.append(i+"\n")
		soup = BeautifulSoup(response.text, 'lxml')

	else:
		print(colorama.Fore.LIGHTRED_EX +'\nAll mails extracted!')

file1 = open("C:\\Users\\anand59\\Desktop\\Promo\\Journal\\JournalMAILS.txt","a+")
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
print(colorama.Fore.LIGHTRED_EX +'\nAll mails extracted!')