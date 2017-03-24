# -*- coding: utf-8 -*-
import datetime
import json

from model.player   import Player
from model.admin    import Admin, Moderator
from model.session  import Session
from model.money    import Money, Wallet,GOLD,SILVER,COPPER



if __name__=="__main__":


    player = Player(nickname='Arseni', email='arsenidudko@mail.ru', password='14332dwa5')
    print("{}Information about the player.\n".format(player))
    player.save_to_db()
    print("{}Player was inserted to db.\n".format(player))


    admin = Admin(nickname='admin_arseni', email='arseniadmin@mail.ru', password='14dsads332dwa5')
    print("{}Information about the player.\n".format(admin))
    admin.save_to_db()
    print("{}Admin was inserted to db.\n".format(admin))


    moderator = Moderator(nickname='moderator_arseni', email='arsenimoderator@mail.ru', password='1dsadsa13')
    print("{}Information about the player.\n".format(moderator))
    moderator.save_to_db()
    print("{}Moderator was inserted to db.\n".format(moderator))


    player_info = Player()
    player_info.load_from_db("arsenidudko@mail.ru")
    print("{}Player was loaded from db.\n".format(player_info))


    player_changes = Player()
    player_changes.load_from_db("arsenidudko@mail.ru")
    player_changes.nickname = "Lesha"
    player_changes.save_to_db()
    print("{}Player was updated in db.\n".format(player_changes))


    player_changes.delete_from_db()
    print("{}Player was deleted from db.\n".format(player_changes))

########################################################################################################################

    player_session = Session(player_id=1, finish_time=datetime.datetime(2017, 2, 14, 00, 00),
                             elapse_time=datetime.datetime(1, 1, 1),
                             created=datetime.datetime.now(), updated=datetime.datetime.now())
    print("{}Information about player session.\n".format(player_session))


    player_session.save_to_db()
    print("{}Player session was inserted to db.\n".format(player_session))


    player_session_info = Session()
    player_session_info.load_from_db(1)

    player_session_change = Session()
    player_session_change.load_from_db(1)
    player_session_change.finish_time = datetime.datetime(2016, 2, 14, 00, 00)
    player_session_change.elapse_time = datetime.datetime(1,1,2)
    player_session_change.save_to_db()
    print("{}Player session was updated in db.\n".format(player_session_change))

########################################################################################################################


    player_money = Money(player_id=1, code = 1, amount = 1000,
                         created=datetime.datetime.now(), updated=datetime.datetime.now())
    print("{}Information about player money.\n".format(player_money))

    player_money.save_to_db()
    print("{}Player money was inserted to db.\n".format(player_money))


    player_money.load_from_db(1)
    player_money.amount = 10000
    player_money.save_to_db()
    print("{}Player session was updated in db.\n".format(player_money))

