print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('')
print("Initializing Dependencies...")
import smtplib
from email.message import EmailMessage
import time
import random
import colorama
colorama.init()
emailsList = open("C:\\Users\\anand59\\Desktop\\Promo\\Mailing\\Mailing.txt", "r")
currentEmailList = emailsList.readlines()
print(colorama.Fore.LIGHTGREEN_EX + "Email id: ", end='')
username = str(input("~ "))
password=''
if username=='newsletter.corporatelaw@gmail.com':
	password = "advlucky@1"
else:
	password = "advanand@1"
From = username
print(colorama.Fore.LIGHTGREEN_EX + "Subject: ", end='')
Subject = str(input("~ "))
print(colorama.Fore.LIGHTGREEN_EX + "File Name: ", end='')
emailText = open("C:\\Users\\anand59\\Desktop\\Promo\\Mailing\\"+str(input("~ "))+'.txt', "r+")
emails = emailText.readlines()
for i in range(len(emails)):
	emails[i]=emails[i].replace("\n", '')
print(colorama.Fore.LIGHTWHITE_EX+"Starting Server... \n")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
print(colorama.Fore.LIGHTRED_EX + 'Sending Mails... \n')
for i in range(len(emails)):
	msg = EmailMessage()
	msg['From'] = username
	msg['Subject'] = Subject
	msg['To'] = emails[i]
	htmlContent = '''\
<p style="margin: 0in 0in 0.0001pt; font-size: 15px; font-family: Calibri, sans-serif; line-height: 2;"><strong><span style="font-size: 15px; font-family: Arial, Helvetica, sans-serif;">Dear Sir / Ma&rsquo;am,</span></strong></p>
<p style="margin: 0in 0in 0.0001pt; font-size: 15px; font-family: Calibri, sans-serif; text-align: justify; line-height: 1.15;"><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(29, 34, 40);">We are associated and serving over 500 Pharma firms along with many other companies, and have registered <strong>6000+</strong> brands / trademarks. We are Delhi based law firm, operating since 1997 with a team of experts providing services related to Trademarks and other legal issues, across the nation.</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(29, 34, 40);">Our services are excellent and less expensive (starts from just&nbsp;</span><strong><span style="color: rgb(0, 176, 80);">Rs.1,000/-</span></strong><span style="color: rgb(29, 34, 40);">). Believe us, with our assistance &amp; support, you can have a better management of your brand / trademark, like others.&nbsp;</span></span></span></p>
<p style="margin: 0in 0in 0.0001pt; font-size: 15px; font-family: Calibri, sans-serif; text-align: justify; line-height: 2;"><span style="font-size: 15px;"><span style="font-family: Arial, Helvetica, sans-serif;"><strong>We can:</strong></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(15, 36, 62);">Compensate you and stop others from copying your mark <strong>(</strong></span><strong><span style="color: rgb(152, 72, 6);">Infringement</span></strong><strong><span style="color: rgb(15, 36, 62);">)</span></strong><span style="color: rgb(15, 36, 62);">,</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(15, 36, 62);">Cancel registration of other marks affecting your business, <strong>(</strong></span><strong><span style="color: rgb(152, 72, 6);">Cancellation &amp; Invalidation</span></strong><strong><span style="color: rgb(15, 36, 62);">)</span></strong><span style="color: rgb(15, 36, 62);">,</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(15, 36, 62);">Stop others registering similar to your brand / mark <strong>(</strong></span><strong><span style="color: rgb(152, 72, 6);">Opposition &amp; Counter Statement</span></strong><strong><span style="color: rgb(15, 36, 62);">)</span></strong><span style="color: rgb(15, 36, 62);">,</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(15, 36, 62);">Update you for a timely Renewal and other compliances,</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(15, 36, 62);">Sale-Purchase, Acquiring, Assignment of brand/Trademark for you,</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(15, 36, 62);">Do hearing &amp; Arguments before Trademark Authorities &amp; Court.</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(15, 36, 62);">Renew Registered brand / trademark (only&nbsp;</span><strong><span style="color: rgb(0, 176, 80);">@Rs.1,000/-</span></strong><strong><span style="color: rgb(15, 36, 62);">)</span></strong><span style="color: rgb(15, 36, 62);">,&nbsp;</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(15, 36, 62);">For making Change in details of brand / trademark, &nbsp;</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(15, 36, 62);">File application for Trademark, Logo, Label Registration,</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(15, 36, 62);">File Replies against Official Objections,</span></span></span></p>
<p style="margin: 0in 0in 0.0001pt; font-size: 15px; font-family: Calibri, sans-serif; text-align: center; line-height: 2;"><span style="font-size: 15px;"><span style="font-family: Arial, Helvetica, sans-serif;"><strong><span style="color: red;">FOR REQUIREMENT RELATED WITH BRAND / TRADEMARK,&nbsp;</span></strong></span></span></p>
<p style="margin: 0in 0in 0.0001pt; font-size: 15px; font-family: Calibri, sans-serif; text-align: center; line-height: 1;"><span style="font-size: 15px;"><span style="font-family: Arial, Helvetica, sans-serif;"><strong><span style="color: red;">Feel free to call or email for consultation, status &nbsp;</span></strong></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(29, 34, 40);">Your queries will be responded within 1 hour whereas prosecution will begin the same day.&nbsp;</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><span style="color: rgb(29, 34, 40);">We are - prudent, less expensive, always available, Transparent with Hassle Free 24x7 PAN India Working, a very Large clientage, Regular Court Exposure, Hundreds of national &amp; international reputed brands</span><span style="color: rgb(34, 34, 34);">.</span></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";text-align:justify;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><strong><span style="color: rgb(29, 34, 40);">Post Lockdown situation, on request, we can even assist &amp; work for you on rebates up to (for Indian entities only)-&nbsp;</span></strong></span></span></p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:10.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri","sans-serif";text-align:center;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><strong><span style="line-height: 115%; color: rgb(112, 48, 160);">Trademark filing @Rs.1,000/- &nbsp; &nbsp; &nbsp; Objection-Reply @Rs.1,200/- &nbsp; &nbsp; &nbsp; Hearing @Rs.2,000/-&nbsp;</span></strong></span></span></p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:10.0pt;margin-left:0in;line-height:115%;font-size:15px;font-family:"Calibri","sans-serif";text-align:center;'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><br></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><strong>Shrestha Legal &amp; Trademarks</strong></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><strong>Email:&nbsp;asguptaadvocate@yahoo.com, slslegal99@gmail.com</strong></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><strong><span style="color: rgb(13, 13, 13);"><a href="https://www.slslegal.com/"><span style="color:#0D0D0D;text-decoration:none;">www.slslegal.com</span></a></span></strong><strong>&nbsp; &nbsp; &nbsp;Phone: &nbsp;9891665001, 838400737</strong></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";'><span style="font-size: 14px;"><span style="font-family: Arial, Helvetica, sans-serif;"><strong>Offices:&nbsp;12, Balaji Complex, Pandav Nagar, Delhi-110092</strong></span></span></p>
<p style='margin:0in;margin-bottom:.0001pt;font-size:15px;font-family:"Calibri","sans-serif";'><strong><span style="font-size: 14px; font-family: Arial, Helvetica, sans-serif;">Off &amp; Res.: 59, Kundan Nagar, Delhi-110092</span></strong></p>
	'''
	msg.add_alternative(htmlContent, subtype='html')
	message = msg.as_string()
	server.sendmail(username, emails[i], message)
	sentTo = 'Mail sent to: ' + emails[i] + ' \n'
	print(colorama.Fore.LIGHTYELLOW_EX + sentTo)
	time.sleep(random.randint(2,6))
server.quit()
print(colorama.Fore.RED + 'All mails sent successfully')
print('')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')