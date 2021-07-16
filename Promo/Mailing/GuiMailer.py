# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print('')
# print("Initializing Dependencies...")

import smtplib
# import openpyxl as xl
# import os
from email.message import EmailMessage
import time
import random
import PySimpleGUI as sg

theme_name_list = sg.theme_list()
sg.theme(random.choice(theme_name_list))
layout = [
	[sg.Text("Send unlimited mails anytime, anywhere!")],
	[sg.Text("\nThe program takes around 5 seconds to start and may lag a bit. Please be patient.")],
	[sg.Text('Email: '), sg.InputText()],
	[sg.Text("Sample Emails: "), sg.InputText('slslegal99@gmail.com, info.slslegal@gmail.com')],
	[sg.Text('Subject: '), sg.InputText()],
	[sg.Text('Mail File name: '), sg.InputText()],
	[sg.Frame('Emails Sent:', font='Any 15', layout=[[sg.Multiline("", size=(70,20), key="protocol", autoscroll=True, disabled=True)],])],
	[sg.Button('Send'), sg.Button('Quit')],
	[sg.Text("\nNote: A letter of the last email is removed due to technical reasons. Your may provide a fake id at the end to avoid this issue.")],
	[sg.Frame('Emails To send:', font='Any 15', layout=[[sg.Multiline("", size=(60,10), key="protocol2", autoscroll=True, disabled=True)]])]]

window = sg.Window("Send unlimited emails!", icon='C:\\Users\\anand59\\Desktop\\Promo\\Mailing\\logo.ico').Layout(layout).Finalize()
window.Maximize()

while True:
	event, values = window.read()
	if event == "Quit" or event == sg.WIN_CLOSED:
		break

	# newList = list(map(lambda x:x.strip(),l))

	if event == "Send":
		try:
			emailsList = open("C:\\Users\\anand59\\Desktop\\Promo\\Mailing\\Mailing.txt", "r")
			currentEmailList = emailsList.readlines()
			# window.FindElement("protocol2").Update(" \n", append=True)
			print(currentEmailList)
			for x in currentEmailList:
				window.FindElement("protocol2").Update(x, append=True)

			username = values[0]
			password = "advanand@1"
			From = username
			Subject = values[2]

			# wb = xl.load_workbook(r'C:\Users\anand59\Desktop\Promo\Mailing\mail.xlsx')
			# sheet1 = wb.get_sheet_by_name('Worksheet')

			emailText = open("C:\\Users\\anand59\\Desktop\\Promo\\Mailing\\"+values[3], "r+")
			emails = emailText.readlines()

			for i in range(len(emails)):
				emails[i]=emails[i][:-1]

			print(emails)

			# for cell in sheet1['A']:
			#	 emails.append(cell.value)

			# for cell in sheet1['A']:
			#	 names.append(cell.value.split('@')[0])

			window.FindElement("protocol").Update("Starting Server... \n", append=True)

			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(username, password)

			window.FindElement("protocol").Update("Sending Mails... \n", append=True)

			for i in range(len(emails)):
				msg = EmailMessage()
				msg['From'] = username
				msg['Subject'] = Subject
				msg['To'] = emails[i]


				htmlContent = '''\
				<div style="background-color: #f0f4f8; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; font-size:1.2rem">
					<img src="https://drive.google.com/uc?export=view&id=1QzFySyUaIWldgq9_ZdNo6wBsgsiiIpAV"
					style="box-shadow:
						0 2.8px 2.2px rgba(0, 0, 0, 0.034),
						0 6.7px 5.3px rgba(0, 0, 0, 0.048),
						0 12.5px 10px rgba(0, 0, 0, 0.06),
						0 22.3px 17.9px rgba(0, 0, 0, 0.072),
						0 41.8px 33.4px rgba(0, 0, 0, 0.086),
						0 100px 80px rgba(0, 0, 0, 0.12); width:100%;">



					<table border="0" cellspacing="5" cellpadding="10" style="width:100%; color:white"> 
						<tbody>
							<tr style="text-align:center; background-color: #fd7014; ">
								<td colspan="4" valign="top" ><h2 style="margin-bottom: -20px;">Outsource your Trademark</h2>
								<h3 style="font-weight: 500;">for better management</h3>
								<h2 style="color:black"><strong>Get your Trademark at just Rs.1,100/- (for Indian firms)</strong></h2></td>
							</tr>
							<tr style="text-align:center; background-color:#222831;">
								<td colspan="4" valign="top" ><h3>OUR TRADEMARK SERVICES (PAN INDIA) </h3>
								<p>Handling 6000+ Trademarks</p>
							</tr>
							<tr style="background-color: #fd7014; ">
								<td colspan="2" valign="top" >
									<p>Trademark, Logo Registration</p>
									<p>Objection - Reply Filing </p>
									<p>Show Cause Hearing for approval </p>
									<p>Opposition of Trademark </p>
									<p>Counter Statement Filing</p>
									<p>Infringement of Trademark</p>
									<p>Trademark Assignment</p>
									<p>Sale – Purchase of mark</p>
									<p>Renewal of Trademark</p>
									<p>Cancellation of Trademark </p>
									<p>Rectification of Trademark</p>
									<p>Change in Trademark detail</p>
									<p>Litigation of Trademark</p>
									<p>Maintenance of Trademark</p>
									<p>MSME Reg. for Trademark </p>
								</td>
								<td colspan="2" valign="top" >
									<center><h2><p>We are</p></h2></center>
									<p>Well Known organization</p>
									<p>Cost Effective services</p>
									<p>Transparent working </p>
									<p>Experienced legal team</p>
									<p>Hassel-free working</p>
									<p>Easy availability</p>
									<p>24 x 7 working</p>
									<p>All India Working </p>
									<p>PAN India Network</p>
									<p>Huge No. of clients </p>
									<p>Handling 6000+ marks </p>
									<p>National &amp; Intl. brands</p>
									<p>Regular Court exposure </p>
								</td>
							</tr>
							<tr style="background-color:#222831; text-align: center">
								<td colspan="4" valign="top" ><h3><strong>Our Subsidized Charges for Trademarks 
								<br>(for Indian Nationals only)</strong></h3></td>
							</tr>
							<tr style="background-color:#222831; text-align: center"">
								<td valign="top" ><p><strong>PLAN I</strong></p></td>
								<td valign="top" ><p><strong>PLAN II</strong></p></td>
								<td valign="top" ><p><strong>PLAN III</strong></p></td>
							</tr>
							<tr style="background-color: #fd7014; text-align: center; font-size:auto">
								<td valign="top" >
									<p>Filing of Application</p>
									<p><strong>1,100/-</strong></p>
									<p>Filing of Reply</p>
									<p><strong>1,100/-</strong></p>
									<p>Attending Hearing</p>
									<p><strong>3,500/-</strong></p>
								</td>
								<td valign="top" >
									<p>Filing of Application</p>
									<p>+ Filing of Reply</p>
									<p><strong><s>2,700/-</s></strong></p>
									<p><strong>2,100/-</strong></p>
									<p>Attending Hearing</p>
									<p><strong>3,500/-</strong></p>
								</td>
								<td valign="top" >
									<p>Filing of Application</p>
									<p>+ Filing of Reply</p>
									<p>+ Attending Hearing</p>
									<p><strong><s>5,700/-</s></strong></p>
									<p><strong>4,500/-</strong></p>
								</td>
							</tr>
							<tr style="background-color:#222831;">
								<td colspan="4" valign="top" >
									<div>Application fee (to deposit with trademark office)
									<br>Rs.4,500/- for Individual/Proprietorship Firm
									<br>Rs.9,000/- for Partnership Firm/Company</div>
								</td>
							</tr>
							<tr>
								<td colspan="4" valign="top" style="text-align:center; background-color: #fd7014; "><p><strong>FREE - Search report + Consultation for application</strong></p></td>
							</tr>
							<tr style="background-color:#222831;">
								<td colspan="4" valign="top" >
									<h3 style="text-align:center">TRADEMARK RENEWAL</h3>
									<p><strong>Our Charges Rs.1,000/-,
									<br>Govt. Fee for Renewal Rs.9,000/-,</strong></p>
									<p>
										<strong>Requirements – </strong>
										<br>1. Trademark Application No.
										<br>2. Expenses.
									</p>
									<p><strong>RENEWAL PROCESS WILL BE COMPLETED BY SAME DAY
										<br>PAYMENT RECEIPT &amp; FILING DETAILS WILL BE SHARED IMMEDIATELY</strong></p>
									<p>We are associated with hundreds of CA, CS, law firms, advocates across the nation</p>
								</td>
							</tr>
							<tr>
							<td colspan="4" style="text-align:center; background-color: #fd7014; "><p><strong>asguptaadvocate@yahoo.com &emsp;
								www.slslegal.com&emsp;
								Ph. 9891665001</strong></p></td>
							</tr>
						</tbody>
					</table>
					<br>
					<br>
					<table cellspacing="0" cellpadding="10" style="width:100%; " > 
						<tbody style="color:white"> 
							<tr>
								<td style="background-color: #fd7014; text-align: center;" colspan="4" valign="top" ><p><strong>We can serve &amp; support you for the following court cases:</strong></p></td>
							</tr>
							<tr colspan="1" style="background-color: #222831;">
								<td>Civil suits</td>
								<td>Cheque Bounce</td>
								<td>Labor Law Cases</td>
								<td>FSSAI Reg.</td>
							</tr>
							<tr colspan="1" style="background-color:#222831;">
								<td>Criminal cases</td>
								<td>Payment Recovery</td>
								<td>Banking &amp; Finance case</td>
								<td>FSSAI Licence</td>
							</tr>
							<tr colspan="1" style="background-color:#222831;">
								<td>Consumer Case</td>
								<td>Arbitration</td>
								<td>Contracts </td>
								<td>Agreements</td>
							</tr>
							<tr colspan="1" style="background-color:#222831;">
								<td>MSME</td>
								<td>ESI &amp; PF</td>
								<td>Legal notices &amp; Compl.</td>
								<td>Company Reg.</td>
							</tr>
						</tbody>
					</table>
					<br>
					<br>
					<table border="0" cellspacing="10" cellpadding="10" style="width:100%; background-color: #fd7014; color: white;" > 
						<tbody >
							<tr style="text-align: center;">
								<td valign="top" ><p><strong>Most Valuable &amp; Important Service (FOR FREE)</strong></p>
									<div>
										<br>We will be giving you regular updates for all your brands -
										<br> * If someone is Copying, infringing, Counterfeiting your mark
										<br> * Its Renewal date has approached,
										<br> Contact immediately for availing this service!
									</div>
								<br>
								</td>
							</tr>
						</tbody>
					</table>
					<br>
					<br>

					<p style="text-align:center"><strong>“आपकी कोई भी कानूनी जरुरत हो - हमसे पूछिये”</strong></p>

				</div>
				'''

				msg.add_alternative(htmlContent, subtype='html')

				message = msg.as_string()
				server.sendmail(username, emails[i], message)
				sentTo = 'Mail sent to' + emails[i] + ' \n'
				window.FindElement("protocol").Update( sentTo, append=True)

				time.sleep(random.randint(2,4))

			server.quit()
			window.FindElement("protocol").Update("\n All emails sent successfully! \n", append=True)
		except:
			window.FindElement("protocol").Update("\n ~ An error occured. limit exceeded, try again later or use a different account. ~ \n", append=True)
window.close()