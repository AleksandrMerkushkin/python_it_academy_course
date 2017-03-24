# -*- coding: utf-8 -*-
import smtplib
smtp_obj = smtplib.SMTP('smtp.mail.ru', 587)
print(smtp_obj.ehlo())
print smtp_obj.starttls()
print smtp_obj.login('arsenidudkotest@mail.ru', 'd6d5bd92')
print smtp_obj.sendmail('arsenidudkotest@mail.ru', 'arsenidudko@mail.ru',
'Subject: Hello.\n\nHello out of Python! How are you??:). Email Bot.')
print smtp_obj.quit()