import smtplib
import ssl
from email.message import EmailMessage 

subject = "Email From Python"
body = "This is a test email form python!"
sender_email = "coderacerlivestreamapp@gamail.com"
reciever_email = "coderacerlivestreamapp@gamail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] =sender_email
message["To"] = reciever_email
message["Subject"] = subject
message.set_content(body)



context = ssl.create_default_context()

print("Sending Email")

with smtplib.SMTP_SSl("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email,receiver_email, message.as_string())

print("Success")