# -*- coding: utf-8 -*-
import smtplib
from email.message import Message
from email.header import Header
msg = Message()
msg.set_charset("utf-8")
h = Header(u'Привет, Медвед!'.encode('utf-8'), 'utf-8')
msg["Subject"] = h
text = u'Юникодный текст :)'
msg.set_payload(text.encode('utf-8'))
smtp_obj = smtplib.SMTP('smtp.mail.ru', 587)
print smtp_obj.starttls()
print smtp_obj.login('arsenidudkotest@mail.ru', 'd6d5bd92')
print smtp_obj.sendmail('arsenidudkotest@mail.ru', 'arsenidudko@mail.ru', msg.as_string())
print smtp_obj.quit()