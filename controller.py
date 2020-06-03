import sys
import smtplib
from email.message import EmailMessage
import csv
import os.path
def control(name,organisation,phone,email,message):
	handle(name,organisation,phone,email,message)
	subject = "You have a message from {} of {}".format(name,organisation)
	from_addr = "aazar@marketbetter.in"
	to_addrs = "order@igroomup.in"
	body = '''{} from {} with phone number {} and email {} has sent the below message by website:\n {}'''.format(name,organisation,phone,email,message)
	msg = EmailMessage()
	msg.set_content(body)
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = to_addrs
	server = smtplib.SMTP('mail.marketbetter.in')
	server.login("glamfleet@marketbetter.in", "iplaytowin")
	server.send_message(msg)
	server.quit()
	
def handle(name,organisation,phone,email,message):
	data = [{
		"Name" : name,
		"Organisation" : organisation,
		"Phone" : phone,
		"Email" : email,
		"Message" : message
	}]
	if os.path.isfile('data.csv'):
		f = open("data.csv", "a")
		writer = csv.DictWriter(
		    f, fieldnames=["Name","Organisation","Phone","Email","Message"])
		writer.writerows(data)
		f.close()
	else:
		f = open("data.csv", "w")
		writer = csv.DictWriter(
		    f, fieldnames=["Name","Organisation","Phone","Email","Message"])
		writer.writeheader()
		writer.writerows(data)
		f.close()