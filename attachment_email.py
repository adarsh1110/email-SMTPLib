import smtplib
from email.message import EmailMessage

sender_email = "sender email ID"
sender_pass = "sender password"

receiver = 'receiver1@gmail.com', 'receiver2@gmail.com'

msg = EmailMessage()
msg['Subject'] = 'Email send of the subject'
msg['From'] = sender_email
msg['To'] = receiver
msg.set_content('Body of the email')

files = ['file.pdf', 'file.jpg']

for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data,maintype = 'application', subtype = 'octer-stream', filename = file_name)

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login(sender_email,sender_pass)
smtp.send_message(msg)