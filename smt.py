#Program to send an email to my friend

#Importing smtp library package
import smtplib

s=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for security
s.starttls()

#Authentication
s.login("sazcmrece56@gmail.com", "ubuntu123$cmru")

#Message TO BE SENT 
message = "Hey ,how r u?...."

#Sending an email
s.sendmail("sazcmrece56@gmail.com" , "vinay123654789@gmail.com", message)
print("message has been SENT")
#Terminating the session
s.quit()