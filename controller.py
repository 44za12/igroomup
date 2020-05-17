import sys
import smtplib
from email.message import EmailMessage
import csv
import os.path
def control(company,name,emailaddress,role,jobtype):
	handle(company,name,emailaddress,role,jobtype)
	subject = "{} wants to hire you!".format(company)
	from_addr = "glamfleet@marketbetter.in"
	to_addrs = "perfectaazar@gmail.com"
	body = '''{} from {} wants to hire you for {} on a {} basis!\nIf I were you (wait I am you) I'd contact him right away!'''.format(name,company,role,jobtype)
	msg = EmailMessage()
	msg.set_content(body)
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = to_addrs
	server = smtplib.SMTP('mail.marketbetter.in')
	server.login("glamfleet@marketbetter.in", "iplaytowin")
	server.send_message(msg)
	server.quit()
	
def handle(company,name,emailaddress,role,jobtype):
	data = [{
		"Company" : company,
		"Name" : name,
		"Email" : emailaddress,
		"Role" : role,
		"Job Type" : jobtype
	}]
	if os.path.isfile('data.csv'):
		f = open("data.csv", "a")
		writer = csv.DictWriter(
		    f, fieldnames=["Company", "Name", "Email", "Role", "Job Type"])
		writer.writerows(data)
		f.close()
	else:
		f = open("data.csv", "w")
		writer = csv.DictWriter(
		    f, fieldnames=["Company", "Name", "Email", "Role", "Job Type"])
		writer.writeheader()
		writer.writerows(data)
		f.close()