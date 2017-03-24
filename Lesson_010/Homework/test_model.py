# -*- coding: utf-8 -*-
import json
import datetime

from model.player   import Player
from model.admin    import Admin, Moderator
from model.session  import Session
from model.money    import Money, Wallet,GOLD,SILVER,COPPER



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