# -*- coding: utf-8 -*-
import urllib2
import urllib
api_key = '4431f07e-e49d-5734-a55c-bf5e0fc6b011'
phone = '375291175345'
url_template = 'http://sms.ru/sms/send?api_id=%(api_key)s&to=%(phone)s'
url = url_template % {"api_key": api_key, "phone": phone}
text = u'Hello, медвед!!'
encoded_text = urllib.urlencode({"text": text.encode('utf-8') })
headers = {"Content-type":"application/x-www-form-urlencoded",}
r = urllib2.Request(url, data=encoded_text, headers=headers)
u = urllib2.urlopen(r)
u.read()