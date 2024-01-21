import os
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

HOST = "smtp.gmail.com"
PORT = 587
FROM_EMAIL = input("enter your mail: ")

TO_EMAIL = input("enter mail you want to send a file: ")
PASSWORD = getpass.getpass(prompt='Enter your Password of mail: ',stream=None)
message = ' hello '
smtp = smtplib.SMTP(HOST,PORT)
smtp.starttls()

smtp.login(FROM_EMAIL,PASSWORD)
print("Good login")
smtp.send_message(FROM_EMAIL,TO_EMAIL,message)
print('Message has been sent')


status, response = smtp.ehlo()
print(f"Echoing Server: {status}, {response}")
status,response = smtp.login(FROM_EMAIL,PASSWORD)
print(f"Logging in: {status} {response}")
path = r'C:\Users\zirko\Documents\skcu'
file_list = os.listdir(path)
msg = MIMEMultipart()
for file_name in file_list:
    file_path = os.path.join(path,file_name)

    with open(file_path,'rb') as attachment:
        file_part = MIMEApplication(attachment.read(),Name=file_name)
        file_part['Content-Disposition'] = f'attachment; filename={file_part["Name"]}'
        msg.attach(file_part)
    try:
        with smtplib.SMTP(HOST, PORT) as server:
            # server.starttls()
            server.login(FROM_EMAIL, PASSWORD)

            server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())

        print(f'Письмо с файлом {file_name} успешно отправлено!')

    except Exception as e:
        print(f'Ошибка при отправке письма с файлом {file_name}: ')

    finally:
        msg.clear_attachments()
        print('Все письма успешно отправлены!')

