# -*- coding: utf-8 -*-
import os
import re
import json
import datetime

GOLD = 1
SILVER = 2
COPPER = 3



class Player(object):
    def __init__(self, name=None, email=None, password=None, wallet=None, session=None):
        self.name = name
        self.email = email
        self.password = password
        self.wallet = wallet
        self.session = session

        # For take_money, give_money methods
        self.gold = gold
        self.silver = silver
        self.copper = copper
        self.money = {
            GOLD: gold,
            SILVER: silver,
            COPPER: copper
        }

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

    def as_dict(self):
        d = {
            "name":self.name,
            "email":self.email,
            "password":self.password,
            "wallet":self.wallet.as_dict(),
            "session":self.session

        }
        return d

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


class Moderator(Player):
    def __init__(self, name, email, password, wallet):
        super(Moderator, self).__init__(name, email, password, wallet)
        self.type = 'Moderator'

    def ban_player(self, file_object, username):
        file = open(file_object).read()
        if username in file:
            if (re.search(ur'\w{0}|{0}\w'.format('banned_'), file)):
                print u'Player {} has been already banned!'.format(username)
            else:
                print u"Player {} was banned by {}".format(username, self.name)
                print u'Changing "{username}" to banned_{username}'.format(**locals())
                file = file.replace(username, str("banned_" + username))
                f = open(file_object, 'w')
                f.write(file)
                f.flush()
                f.close()
        else:
            print u'No occurances of "{username}" found.'.format(**locals())

    def unban_player(self, file_object, username):
        file = open(file_object).read()
        if username in file:
            if (re.search(ur'\w{0}|{0}\w'.format('banned_'), file)):
                print u"Player {} has been unbanned by {}".format(username, self.name)
                print u'Changing banned_{username} to {username}'.format(**locals())
                file = file.replace(str("banned_" + username), username)
                f = open(file_object, 'w')
                f.write(file)
                f.flush()
                f.close()
            else:
                print u"Player {} is unban!".format(username)
        else:
            print u'No occurances of "{username}" found.'.format(**locals())

    def report_player(self, file_object, username):
        file = open(file_object, "r")
        for line in file.readlines():
            us, pw, rp = line.strip().split("|")
            if ('banned_' + username) in us:
                print u'Player {} is already blocked!'.format(username)
                return False
            if username == us:

                if int(rp) >= 3:
                    print 'User has been reported many times and will be banned!'
                    print u"Player {} was banned by {}".format(username, self.name)
                    print u'Changing "{username}" to banned_{username}'.format(**locals())
                    file_data = open(file_object).read()
                    new_file = file_data.replace(username, str("banned_" + username)).replace(str('|' + rp), "|0")
                    f = open(file_object, 'w')
                    f.write(new_file)
                    f.flush()
                    f.close()
                if int(rp) < 3:
                    new_rp = int(rp) + 1
                    print 'User will be reported!'
                    print u"Player {} has been reported by {}".format(username, self.name)
                    print u"Total reports {}!".format(int(rp)+1)
                    filedata = open(file_object).read()
                    new_file = filedata.replace((str(username) + '|' + str(pw) + '|' + str(rp)),
                                           (str(username) + '|' + str(pw) + '|' + str(new_rp)))
                    f = open(file_object, 'w')
                    f.write(new_file)
                    f.flush()
                    f.close()


    def display_target_balance(self, file_object):
        object_as_dict = json.load(file_object)
        gold = Money(code=object_as_dict["wallet"]["gold"]["code"],
                     amount=object_as_dict["wallet"]["gold"]["amount"])

        silver = Money(code=object_as_dict["wallet"]["silver"]["code"],
                       amount=object_as_dict["wallet"]["silver"]["amount"])

        copper = Money(code=object_as_dict["wallet"]["copper"]["code"],
                       amount=object_as_dict["wallet"]["copper"]["amount"])

        self.wallet = Wallet(gold, silver, copper)
        return '          %s' % self.wallet

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
        os.remove(player_name)
        return u"\n#################################################\n" \
               u"{}\n\n" \
               u"Has been deleted by {}" \
               u"\n#################################################\n" \
               .format(player_name, self.name)



class Session():
    def __init__(self):
        self.start_time = datetime.datetime.now()

    def start(self):
        self.start_time = datetime.datetime.now()
        return self.start_time

    def end(self):
        self.end_time = datetime.datetime.now()
        return self.end_time

    def get_elapse_time(self):
        elapsedTime = None
        if self.start_time is not None:
            if self.end_time is not None:
                elapsedTime = (self.end_time) - \
                              (self.start_time)

        else:
            rightNow = datetime.datetime.now()
            elapsedTime = (rightNow - rightNow)
        return (elapsedTime)

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

    def __str__(self):
        return u'Starting : {};\n' \
               u'Finished : {};'.format(self.start_time, self.finish_time)

class Wallet():
    def __init__(self,gold, silver, copper):

        if gold.code != GOLD:
            raise Exception("gold.code != GOLD")
        if silver.code != SILVER:
            raise Exception("silver.code != SILVER")
        if copper.code != COPPER:
            raise Exception("copper.code != COPPER")

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
            "gold":   self.gold.as_dict(),
            "silver": self.silver.as_dict(),
            "copper": self.copper.as_dict()
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.gold = object_as_dict["gold"]
        self.silver = object_as_dict["silver"]
        self.copper = object_as_dict["copper"]
        return object_as_dict

    def __str__(self):
        return u'Gold   - {};' \
               u'\n           Silver - {};' \
               u'\n           Copper - {};'.format(self.gold, self.silver, self.copper)


class Money():
    def __init__(self,code, amount):
        self.code = code
        self.amount = amount

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

    def __str__(self):
        return u'currency_code:{}, amount:{}'.format(self.code, self.amount)




if __name__=="__main__":

    gold   = Money(code=1, amount=10)
    silver = Money(code=2, amount=100)
    copper = Money(code=3, amount=1000)
    wallet = Wallet(gold,silver,copper)


    arseni = Player(name = 'Arseni', email = 'arsenidudko@mail.ru', password = '123456', wallet=wallet)
    arseni.save(open("arseni_player.txt", "w"))
    print(u"Player is:"
          u"\n#################################################\n" \
          u"{}"
          u"\n#################################################\n".format(arseni))


    arseni2 = Player(name = 'Arseni2', email = 'arsenidudko2@mail.ru', password = '765432', wallet=wallet)
    arseni2.load(open("arseni_player.txt"))
    print(u"Deserialized player is:"
          u"\n#################################################\n" \
          u"{}"
          u"\n#################################################\n".format(arseni2))

########################################################################################################################

    print u"Login, logout methods"
    print u"!!!See users and passwords in users.txt!!!", '\n'
    arseni.log_in()
    arseni.log_out()
    print '\n'

########################################################################################################################

    print u"Take_money, give_money methods"
    print '\n'
    wallet =  Wallet(gold,silver,copper)
    print u'Player Arseni \n'
    arseni.display_balance()

    while True:
        try:
            #Pick an option to withdraw, deposit or exit
            print("1: Deposit funds")
            print("2: Withdraw funds")
            print("3: Exit")

            type = int(input("Please select an option (1, 2 or 3): "))
            if type == 1:
                currency_type =  input("Please specify type of currency to deposit GOLD, SILVER or COPPER: ")
                deposit_amount =  int(input("Please specify amount of currency to deposit: "))
                arseni.deposit(currency_type, deposit_amount)
                print '\n'
                arseni.display_balance()

            elif type == 2:
                currency_type =  input("Please specify type of currency to withdraw GOLD, SILVER or COPPER: ")
                withdraw_amount = int(input("Please specify amount of currency to withdraw: "))
                arseni.withdraw(currency_type, withdraw_amount)
                print '\n'
                arseni.display_balance()
            elif type == 3:
                break
            else:
                print("Invalid selection, please type either 1,2 or 3")
        except SyntaxError:
            print '\n####################################\n' \
                  'You have typed  nothing.\n' \
                  'Try again or type 3 to exit...\n'

########################################################################################################################

    gold   = Money(code=GOLD,   amount=9999)
    silver = Money(code=SILVER, amount=99999)
    copper = Money(code=COPPER, amount=999999)

    admin_wallet = Wallet(gold, silver, copper)


    Alex  = Admin(name='Alex', email='admin_alex@mail.ru', password='1234567', wallet=admin_wallet)
    Alex2 = Moderator(name='Alex2', email='moderator_alex@mail.ru', password='12345dsa67', wallet=admin_wallet)

    print(u"Administrator:"
          u"\n#################################################\n" \
          u"{}"
          u"\n#################################################\n".format(Alex))
    Alex.save(open("admin_alex.txt", "w"))

    Alex.ban_player("users.txt", 'arseni2')
    print'\n'
    Alex.unban_player("users.txt", 'arseni2')
    # Alex.delete_player("arseni_player.txt")

    print(u"Moderator:"
          u"\n#################################################\n" \
          u"{}"
          u"\n#################################################\n".format(Alex2))
    Alex2.save(open("moderator_alex.txt", "w"))

    Alex2.report_player("users.txt", "arseni3")
########################################################################################################################

    print u"\n Admin menu", '\n'
    file_object = u'arseni_player.txt'
    print u'File object: {}'.format(file_object)
    print u'Balance:\n {}'.format(Alex.display_target_balance(open(file_object, "r"))), '\n'
    with open(file_object, 'r+') as logger:
        object_as_dict = json.load(logger)
        save_file = Alex.save(open(file_object, "w"))
        try:
            while True:
                # Pick an option to modify player or exit
                print(u"1: Player info")
                print(u"2: Change player name")
                print(u"3: Change player password")
                print(u"4: Change player email")
                print(u"5: Change player gold")
                print(u"6: Change player silver")
                print(u"7: Change player copper")
                print(u"8: Save changes")
                print(u"9: Exit"), '\n'

                type = int(raw_input(u"Please select an option (1,2,3,4,5,6,7,8 or 9): "))

                if type == 1:
                    print  u"\nFile object is {}\n".format(file_object)
                    print  u"Name     : {}".format(object_as_dict["name"])
                    print  u"Password : {}".format(object_as_dict["password"])
                    print  u"Email    : {}".format(object_as_dict["email"])
                    print  u"Gold     : {}".format(object_as_dict["wallet"]["gold"]["amount"])
                    print  u"Silver   : {}".format(object_as_dict["wallet"]["silver"]["amount"])
                    print  u"Copper   : {}".format(object_as_dict["wallet"]["copper"]["amount"]), '\n'

                elif type == 2:
                    with open(file_object, 'w') as logger:
                        object_as_dict["name"] = raw_input(u"Modify name of player: ")
                        json.dump(object_as_dict, logger)
                        logger.close()
                    print '\n'
                elif type == 3:
                    with open(file_object, 'w') as logger:
                        object_as_dict["password"] = raw_input(u"Modify password of player: ")
                        json.dump(object_as_dict, logger)
                        logger.close()
                    print '\n'
                elif type == 4:
                    with open(file_object, 'w') as logger:
                        object_as_dict["email"] = raw_input(u"Modify email of player: ")
                        json.dump(object_as_dict, logger)
                        logger.close()
                    print '\n'
                elif type == 5:
                    with open(file_object, 'w') as logger:
                        object_as_dict["wallet"]["gold"]["amount"] = int(input(u"Modify gold of player: "))
                        json.dump(object_as_dict, logger)
                        logger.close()
                    print '\n'
                elif type == 6:
                    with open(file_object, 'w') as logger:
                        object_as_dict["wallet"]["silver"]["amount"] = int(input(u"Modify silver of player: "))
                        json.dump(object_as_dict, logger)
                        logger.close()
                    print '\n'
                elif type == 7:
                    with open(file_object, 'w') as logger:
                        object_as_dict["wallet"]["copper"]["amount"] = int(input(u"Modify copper of player: "))
                        json.dump(object_as_dict, logger)
                        logger.close()
                    print '\n'
                elif type == 8:
                    print Alex.modify_player(file_object)
                    save_file
                    print '\n'
                elif type == 9:
                    print Alex.modify_player(file_object)
                    break
                    print '\n'
                else:
                    print(u"Invalid selection, please type either 1,2,3,4,5,6,7,8 or 9")
                    print '\n'
        except ValueError:
            print 'Invalid input! Try again'
        except NameError:
            print 'Invalid input of integer! Try again'

########################################################################################################################

    print 'Delete method'
    print Alex.delete_player("arseni_player.txt")

