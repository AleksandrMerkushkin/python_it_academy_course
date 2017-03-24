# -*- coding: utf-8 -*-
import json
import datetime

from money      import Money, Wallet, GOLD, SILVER, COPPER
from session    import Session


class Player(object):
    def __init__(self, name=None, email=None, password=None, wallet=None, session=None):
        self.name = name
        self.email = email
        self.password = password
        self.wallet = wallet
        self.session = session

        # For checking take_money and give_money methods
        gold = Money(code=1, amount=10)
        silver = Money(code=2, amount=100)
        copper = Money(code=3, amount=1000)

        self.gold = gold
        self.silver = silver
        self.copper = copper
        self.money = {
            GOLD: gold,
            SILVER: silver,
            COPPER: copper
        }

    def as_dict(self):
        d = {
            "name":self.name,
            "email":self.email,
            "password":self.password,
            "wallet":self.wallet.as_dict(),
            "session":self.session
        }

        return d

    def log_in(self):

        starting = Session()
        self.session = starting

        user = str(raw_input("Please input username: "))
        passw = raw_input("Please input password: ")
        reports_limit = 3

        if not user:
            print "You need to enter login and password!..."
            return False
        if not passw:
            print "You need to enter login and password!..."
            return False

        file = open("users.txt", "r")
        for line in file.readlines():
            us, pw, rp = line.strip().split("|")
            if ('banned_' + user) in us:
                print 'User was banned!'
                return False
            if (int(rp) >= reports_limit):
                print 'User has been reported many times and banned!'
                return False

            if (user in us) and (passw in pw) and (int(rp) < reports_limit):
                print "Login successful!"
                print u"Starting of game session: {}".format(self.session.start()), '\n'
                return True
            else:
                print "Wrong username/password"
                return False

    def log_out(self):
        ending = Session()
        self.session = ending
        any_key = raw_input("...please enter to exit session")
        print u'User has logged out: {}'.format(self.session.end()), '\n'
        print u'Elapsed time of session: {}'.format(self.session.get_elapse_time())

    def deposit(self, code, amount):
        self.money[code].amount += amount

    def withdraw(self, code, amount):
        if amount <= self.money[code].amount:
            self.money[code].amount -= amount
        else:
            print u"Insufficient funds. You have : {} in your account. Please deposit more or withdraw less." \
                .format(self.money[code].amount)

    def display_balance(self):
        for key in self.money:
            if key == 1:
                print u"The current balance of GOLD   in the account is: {}".format(self.money[key])
            if key == 2:
                print u"The current balance of SILVER in the account is: {}".format(self.money[key])
            if key == 3:
                print u"The current balance of COPPER in the account is: {}".format(self.money[key])
                print '\n'

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.name = object_as_dict["name"]
        self.email = object_as_dict["email"]
        self.password = object_as_dict["password"]
        self.password = object_as_dict["session"]


        gold = Money(code=object_as_dict["wallet"]["gold"]["code"],
                     amount=object_as_dict["wallet"]["gold"]["amount"])

        silver = Money(code=object_as_dict["wallet"]["silver"]["code"],
                       amount=object_as_dict["wallet"]["silver"]["amount"])

        copper = Money(code=object_as_dict["wallet"]["copper"]["code"],
                       amount=object_as_dict["wallet"]["copper"]["amount"])

        self.wallet = Wallet(gold, silver, copper)
        return object_as_dict

    def __str__(self):
        return u'Name     : {};\n' \
               u'Email    : {};\n' \
               u'Password : {};\n' \
               u'Wallet   : {}'.format(self.name, self.email, self.password, self.wallet)

