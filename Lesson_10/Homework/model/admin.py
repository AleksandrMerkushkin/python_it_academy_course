# -*- coding: utf-8 -*-
import re
import os
import json

from player import Player
from money  import Money, Wallet



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

    def openPlayer(self, file_object):
        with open(file_object, 'r+') as logger:
            object_as_dict = json.load(logger)


    def modify_player(self, player_name):
        self.player_name = player_name
        return u"\n#################################################\n" \
               u"{}\n\n" \
               u"Has been modified by {}" \
               u"\n#################################################\n" \
            .format(player_name, self.name)

    def delete_player(self, player_name):
        self.player_name = player_name
        os.remove(player_name)
        return u"\n#################################################\n" \
               u"{}\n\n" \
               u"Has been deleted by {}" \
               u"\n#################################################\n" \
            .format(player_name, self.name)