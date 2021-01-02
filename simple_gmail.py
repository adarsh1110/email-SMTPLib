#Simple single email send to gmail
import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication
sender_email = "sender email ID"
sender_pass = "sender password"
s.login(sender_email, sender_pass )

# contact to be sent
subject = "subject line of email"
body = """
    body of the email
        """

message = f'Subject:{subject}\n\n {body}'

# sending the mail
receiver_email = "receiver@gmail.com"
s.sendmail(sender_email, receiver_email, message)

# terminating the session 
s.quit() 
