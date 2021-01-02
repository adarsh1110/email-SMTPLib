#Simple multiple email send to gmail

import smtplib

# list of email_id to send the mail
receiver = ["receiver1@gmail.com", "receiver2@gmail.com"]

sender_email = "sender email ID"
sender_pass = "sender password"

for list in receiver:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_pass)
    subject = "subject line of the email"
    body = """
            body of the email
            """

    message = f'Subject:{subject}\n\n {body}'
    s.sendmail(sender_email, list, message)
    s.quit()
