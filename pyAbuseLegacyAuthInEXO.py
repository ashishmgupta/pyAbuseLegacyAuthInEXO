from exchangelib import Credentials, Account
import requests
import os
from pathlib import Path
import re

external_ip = requests.get('https://ident.me').text
print(external_ip)
current_dir = os.getcwd()
creds_file = os.path.join(current_dir, "creds.txt")
if not os.path.isfile(creds_file):
    fp = open('creds_file', 'x')
    fp.close()
    print("Credentials file did not exist. We created a new one. Please populate with username and password separated by || in each line")
    quit()
    
with open(creds_file) as f:
    lines = f.readlines()

for line in lines:
	line = line.rstrip()
	cred = line.split("||")
	username = cred[0]
	password = cred[1]
	print(username)
	print(password)
	credentials = Credentials(username, password)
	account = Account(username, credentials=credentials, autodiscover=True)

	user_folder= current_dir+"/"+username
	Path(user_folder).mkdir(parents=True, exist_ok=True)

	for msg in account.inbox.all().order_by('-datetime_received')[:10]:
		email_content=""
		clean_subject = re.sub('[^A-Za-z0-9]+','', msg.subject )
		msg_folder_to_save =  user_folder +"/"+clean_subject
		msg_contents_file =  msg_folder_to_save +"/msg.txt"
		Path(msg_folder_to_save).mkdir(parents=True, exist_ok=True)
		#print(msg.subject, msg.sender, msg.datetime_received)
		
		email_content += "sender            ={}".format(msg.sender) + "\n"
		email_content += "datetime_sent     ={}".format(msg.datetime_sent)+ "\n"
		email_content += "subject           ={}".format(msg.subject)+ "\n"
		email_content += "text_body         ={}".format(msg.text_body.encode('UTF-8'))+ "\n"
		with open(msg_contents_file, "w+") as f:
			f.write(email_content)
		
		print(email_content)
		print("#" * 80)
		for attachment in msg.attachments:
			fpath = os.path.join(msg_folder_to_save, attachment.name)
			with open(fpath, 'wb') as f:
				f.write(attachment.content)