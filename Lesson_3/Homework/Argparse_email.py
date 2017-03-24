# -*- coding: utf-8 -*-
import argparse
import smtplib


def usage():
    """Return string detailing how this program is used."""
    return '''
    A Command Line Interface (CLI) program to send email.
    If the value to an argument is a file path and the file exists, the file
    will be read line by line and the values in the file will be used.
    When supplying multiple email addresses as an argument, a comma should be
    used to separate them.
    Arguments with spaces should be encolsed in double quotes (").'''

parser = argparse.ArgumentParser(description=usage())

parser.add_argument('-m', '--machine',      action='store',             dest='smtphost',    type=str,
                    help="The name of SMTP host used to send the email")
parser.add_argument('-p', '--port',         action='store',             dest='port',        type=int,
                    help="The name of SMTP host used to send the email")
parser.add_argument('-f', '--from',         action='store',             dest='frm',         type=str,
                    help='Who the email is from.  Only first line of file used if file path provided.')
parser.add_argument('-pa', '--password',    action='store',             dest='pasw',        type=str,
                    help='What is password to email.  Only first line of file used if file path provided.')
parser.add_argument('-t', '--to',           action='store',             dest='to',          type=str,
                    help='Who the email is to be sent to.  One email address per line if file path provided.')
parser.add_argument('-s', '--subject',      action='store',             dest='subject',
                    help='The subject of the email.  Only first line of file used if file path provided.')
parser.add_argument('-b', '--body',         action='store',             dest='body',
                    help='Body of email.  All lines from file used if file path provided.')
args = parser.parse_args()

args.subject = 'Subject: ' + args.subject
args.body = '\n\n' + args.body
msg = args.subject + args.body

smtp_obj = smtplib.SMTP(args.smtphost, args.port)
print(smtp_obj.ehlo())
print smtp_obj.starttls()
print smtp_obj.login(args.frm, args.pasw)
print smtp_obj.sendmail(args.frm, args.to, msg)
print smtp_obj.quit()



# -*- coding: utf-8 -*-
# import smtplib
# smtp_obj = smtplib.SMTP('smtp.mail.ru', 587)
# print(smtp_obj.ehlo())
# print smtp_obj.starttls()
# print smtp_obj.login('arsenidudkotest@mail.ru', 'd6d5bd92')
# print smtp_obj.sendmail('arsenidudkotest@mail.ru', 'arsenidudko@mail.ru',
# 'Subject: Hello.\n\nHello out of Python! How are you??:). Email Bot.')
# print smtp_obj.quit()