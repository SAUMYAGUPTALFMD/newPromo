from selenium import webdriver
from email.message import EmailMessage
import smtplib
import colorama
colorama.init()
print(colorama.Fore.LIGHTCYAN_EX+'Name of brand to search: ', end='')
brandName=input('~ ')
print(colorama.Fore.LIGHTBLUE_EX+'Class: ', end='')
className = str(input('~ '))
print(colorama.Fore.LIGHTGREEN_EX+'Mail id to send the report to: ', end='')
mailName = str(input('~ '))
print(colorama.Fore.LIGHTMAGENTA_EX+'Subject: ', end='')
Subject = str(input('~ '))
print(colorama.Fore.LIGHTRED_EX+'Any content before search report in mail: ', end='')
Additional = str(input('~ '))
username = 'newsletter.corporatelaw@gmail.com'
password = "advlucky@1"
driver = webdriver.Chrome('C:\\Users\\anand59\\Desktop\\Promo\\PublicSearch\\chromedriver.exe')
driver.get('https://ipindiaonline.gov.in/tmrpublicsearch/frmmain.aspx')
driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$DDLFilter']/option[text()='Contains']").click()
nameInput = driver.find_element_by_id("ContentPlaceHolder1_TBWordmark")
nameInput.send_keys(brandName)
classInput = driver.find_element_by_id("ContentPlaceHolder1_TBClass")
classInput.send_keys(className)
btn = driver.find_element_by_id('ContentPlaceHolder1_BtnSearch')
btn.click()
search = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_DivSearchResult"]/table/tbody/tr/td[1]/div/div[2]')
result = search.get_attribute('innerHTML')
driver.close()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
print(colorama.Fore.LIGHTWHITE_EX+'Sending Mail... \n')
msg = EmailMessage()
msg['From'] = username
msg['Subject'] = Subject
msg['To'] = mailName
htmlContent = '<p>'+Additional+'</p><br />' + result
msg.add_alternative(htmlContent, subtype='html')
message = msg.as_string()
server.sendmail(username, mailName, message)
print(colorama.Fore.LIGHTYELLOW_EX+'Mail sent...')