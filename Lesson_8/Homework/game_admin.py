# -*- coding: utf-8 -*-

import json
import datetime
from classtools import AttrDisplay                          # Импортирует обобщенный инструмент

class Player(object):
    def __init__(self, name, email, password, wallet):
        self.name = name
        self.email = email
        self.password = password
        self.wallet = wallet

    def __str__(self):
        return u'Name     : {};\n' \
               u'Email    : {};\n' \
               u'Password : {};\n' \
               u'Wallet   : {}'.format(self.name, self.email, self.password, self.wallet)

    def as_dict(self):
        d = {
            "name":self.name,
            "email":self.email,
            "password":self.password,
            "wallet":self.wallet
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.name = object_as_dict["name"]
        self.email = object_as_dict["email"]
        self.password = object_as_dict["password"]
        self.wallet = object_as_dict["wallet"]
        return object_as_dict



class Moderator(Player):
    def __init__(self, name, email, password, wallet):
        super(Moderator, self).__init__(name, email, password, wallet)
        self.type = 'Moderator'

    def ban_player(self, player_name):
        self.player_name = player_name
        return u"\n#################################################\n" \
               u"{}\n\n" \
               u"Has been banned by {}" \
               u"\n#################################################\n" \
               .format(player_name, self.name)

    def report_player(self, player_name):
        self.player_name = player_name
        return u"\n#################################################\n" \
               u"{}\n\n" \
               u"Has been reported by {}" \
               u"\n#################################################\n" \
               .format(player_name, self.name)

    def __str__(self):
        return u'Type     : {};\n' \
               u'Name     : {};\n' \
               u'Email    : {};\n' \
               u'Password : {};\n' \
               u'Wallet   : {}'.format(self.type, self.name, self.email, self.password, self.wallet)

class Admin(Moderator):
    def __init__(self, name, email, password, wallet):
        super(Admin, self).__init__(name, email, password, wallet)
        self.type = 'Administrator'

    def modify_player(self, player_name):
        self.player_name = player_name
        return u"\n#################################################\n" \
               u"{}\n\n" \
               u"Has been modified by {}" \
               u"\n#################################################\n" \
               .format(player_name, self.name)

    def delete_player(self,player_name):
        self.player_name = player_name
        return u"\n#################################################\n" \
               u"{}\n\n" \
               u"Has been deleted by {}" \
               u"\n#################################################\n" \
               .format(player_name, self.name)



class Session():
    def __init__(self,start_time, finish_time):
        self.start_time = datetime.datetime.now()
        self.finish_time = datetime.datetime.now()

    def __str__(self):
        return u'Starting : {};\n' \
               u'Finished : {};'.format(self.start_time, self.finish_time)

    def as_dict(self):
        d = {
            "start_time":self.start_time,
            "finish_time":self.finish_time,
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.start_time = object_as_dict["start_time"]
        self.finish_time = object_as_dict["finish_time"]
        return object_as_dict



class Wallet():
    def __init__(self,gold, silver, copper):
        self.gold   = gold
        self.silver = silver
        self.copper = copper

    def __str__(self):
        return u'Gold   - {};' \
               u'\n           Silver - {};' \
               u'\n           Copper - {};'.format(self.gold, self.silver, self.copper)

class Money():
    def __init__(self,code, amount):
        self.code = code
        self.amount = amount

    def __str__(self):
        return u'currency_code:{}, amount:{}'.format(self.code, self.amount)

    def as_dict(self):
        d = {
            "code":self.code,
            "amount":self.amount

        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.code = object_as_dict["code"]
        self.amount = object_as_dict["amount"]
        return object_as_dict



if __name__=="__main__":

    gold   = Money(code=1, amount=10)
    silver = Money(code=2, amount=100)
    copper = Money(code=3, amount=1000)
    wallet = Wallet(gold,silver,copper)
    # print wallet,'\n'

    arseni = Player(name = 'Arseni', email = 'arsenidudko@mail.ru', password = '123456', wallet= wallet)
    print arseni,'\n'

    arseniSession = Session(start_time = datetime.datetime.now(), finish_time = datetime.datetime.now())
    print arseniSession,'\n'

    admin = Admin(name = 'admin_Arseni', email = 'admin_arsenidudko@mail.ru', password = 'admin123456', wallet= wallet)
    print admin,'\n'

    moderator = Moderator(name='moderator_Arseni', email='moderator_arsenidudko@mail.ru', password='moderator123456', wallet=wallet)
    print moderator,'\n'


    print moderator.report_player(arseni)
    print moderator.ban_player(arseni)


    print admin.report_player(arseni)
    print admin.modify_player(arseni)
    print admin.ban_player(arseni)
    print admin.delete_player(arseni)


