# -*- coding: utf-8 -*-

import json
import sys
import datetime
import MySQLdb

from money          import Money, Wallet, GOLD, SILVER, COPPER
from session        import Session
from connection_db  import connection, ModelIntegrityError


class Player(object):
    def __init__(self,  id=None,   nickname=None, email=None,   password=None,
                    wallet=None,   session=None,  created=None, updated=None):
        self.id = id
        self.type = 1
        self.nickname = nickname
        self.email = email
        self.password = password
        self.wallet = wallet
        self.session = session
        self.created = created
        self.updated = updated

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
            "id":self.id,
            "type":self.type,
            "nickname":self.nickname,
            "email":self.email,
            "password":self.password,
            "wallet":self.wallet.as_dict(),
            "session":self.session,
            "created":self.created,
            "updated":self.updated,
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
        self.id = object_as_dict["id"]
        self.type = object_as_dict["type"]
        self.nickname = object_as_dict["nickname"]
        self.email = object_as_dict["email"]
        self.password = object_as_dict["password"]
        gold = Money(code=object_as_dict["wallet"]["gold"]["code"],
                 amount=object_as_dict["wallet"]["gold"]["amount"])
        silver= Money(code=object_as_dict["wallet"]["silver"]["code"],
                 amount=object_as_dict["wallet"]["silver"]["amount"])
        copper = Money(code=object_as_dict["wallet"]["copper"]["code"],
                 amount=object_as_dict["wallet"]["copper"]["amount"])
        self.wallet = Wallet(gold, silver, copper)
        self.session = object_as_dict["session"]
        self.created = object_as_dict["created"]
        self.updated = object_as_dict["updated"]
        return object_as_dict

    def load_from_db(self,email):
        """
            Method for loading player instance from DB row
            :param email: Player email for loading all info from db
            :return: None
        """

        cursor = connection.cursor()

        sql_query = """SELECT id, type, nickname, email, password, created, updated
                       FROM Player WHERE email=%(email)s"""

        sql_args = {
            "email": email
        }

        new_list = []

        cursor.execute(sql_query,sql_args)
        db_row = cursor.fetchone()
        for elem in db_row:
            new_list.append(elem)

        print u"\n############################################\n" \
              u"Id       : {}\n" \
              u"Type     : {} (admin or moderator=0, user=1)\n" \
              u"Nickname : {}\n" \
              u"Email    : {}\n" \
              u"Password : {}\n" \
              u"Created  : {}\n" \
              u"Updated  : {}\n" \
              u"############################################\n" \
              u"Was loaded from db.\n".format(new_list[0],new_list[1],new_list[2],new_list[3],
                                              new_list[4],new_list[5],new_list[6])
        self.id       = db_row[0]
        self.type     = db_row[1]
        self.nickname = db_row[2]
        self.email    = db_row[3]
        self.password = db_row[4]
        self.created  = db_row[5]
        self.updated  = db_row[6]

    def save_to_db(self):
        """
            Save all player data to MySQL database.
            If a record with player is not exists, it is inserted.
            If method knows _id of player, it will try to update existing
            db record.

            :return: None
        """
        insert_query = """INSERT INTO Player (type, nickname, email, password, created, updated) VALUES
                (%(type)s, %(nickname)s, %(email)s, %(password)s, now(), now())"""

        update_query = """UPDATE Player SET  type=%(type)s, nickname=%(nickname)s, email=%(email)s,
                            password=%(password)s, updated=now() WHERE id=%(id)s"""

        sql_data = {
            "type"      : self.type,
            "nickname"  : self.nickname,
            "email"     : self.email,
            "password"  : self.password,
            }

        cursor = connection.cursor()
        if self.id is None:
            try:
                cursor.execute(insert_query, sql_data)
                self.id = cursor.lastrowid                  #cursor.fetchone()[0]
            except ModelIntegrityError:
                print("\nDEBUG: an integrity error occured when player\n"
                      "       inserting, it's OK")
                pass
        else:
            sql_data["id"] = self.id
            cursor.execute(update_query, sql_data)

    def delete_from_db(self):
        """
        Method for deleting player from DB. Needs correct _id field.
        Perhaps player should be loaded before using this method.

        :return: None
        """
        cursor = connection.cursor()
        delete_query = "DELETE FROM Player WHERE id=%(id)s"
        sql_data = {
            "id": self.id
        }
        cursor.execute(delete_query, sql_data)

    def __str__(self):
        return u"\n#########################################\n"\
               u'ID       : {};\n' \
               u'Type     : {} (admin or moderator=0, user=1);\n' \
               u'Nickname : {};\n' \
               u'Email    : {};\n' \
               u'Password : {};\n' \
               u'Wallet   : {};\n' \
               u'Session  : {};\n' \
               u'Created  : {};\n' \
               u'Updated  : {};\n' \
               u"#########################################\n" \
               .format(self.id, self.type, self.nickname, self.email, self.password,
                       self.wallet, self.session, self.created, self.updated)









