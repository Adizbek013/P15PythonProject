import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from lesson05 import email_validation


def send_mail(reciever_email, code):
    sender_email = "adizbekkarimov324@gmail.com"
    reciever_email = "adizbekkarimov324@gmail.com"
    subject = "Account activiton"
    message = f'Your activation code is: {code}'

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smpt_username = 'adizbekkarimov324@gmail.com'
    smpt_password = 'egbrvyhowhwbctnt'

    # Create a multipart message and set headers
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = reciever_email
    email_message['Subject'] = subject

    email_message.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smpt_username, smpt_password)
        server.send_message(email_message)





# for email in ('adizbekkarimov324@gmail.com', 'mrzbku@gmail.com', 'muradxanboymatov05@gmail.com'):
#     send_mail(email, code)
#
