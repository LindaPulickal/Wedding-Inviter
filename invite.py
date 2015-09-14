import csv
import sys
import smtplib

#todo : attachment
#todo : credentials
#todo : subject
#todo : batch file and folder

def main():
	"""
		This method sends emails from gmail to people in an invitation file with the given message body and subject.
	"""
	
	fromAddr = sys.argv[1] + '@gmail.com'
	subject = 'Subject: Theresa\'s Engagement'
			
	#Gmail credentials
	username = sys.argv[1]
	password = sys.argv[2]
	
	#Smtp server setup
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	
	with open(sys.argv[3], 'r') as messageFile: #invitation message body
		message = messageFile.read()
		
	with open(sys.argv[4], newline = '') as invitationFile: #guestList
		reader = csv.DictReader(invitationFile)
		for guest in reader:
			#if email column is empty, ignore
			if not guest['Email to']: 
				continue
			#invite for wedding only
			if 'skip' in row['Notes'].lower(): 
				continue
			
			name = guest['Email to'] 
			toAddr = 'lindapulickal@gmail.com' #toAddr = guest['Email'] -- will change
			salutation = 'Dear ' + name
			if guest['Spouse']: 
				salutation = ' & '.join([salutation, guest['Spouse']]) #if spouse exists, append spouse name to salutation
			emailHeaders = subject
			personalMessage = emailHeaders + '\n' + salutation + ',' + '\n\n' + message #email headers is for smtp header. It wont show up in message
			server.sendmail(fromAddr, toAddr, personalMessage)
	server.quit()

if __name__ == '__main__':
	main()