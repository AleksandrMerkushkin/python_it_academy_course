# -*- coding: utf-8 -*-
import json
import sys

import datetime
import MySQLdb

from connection_db  import connection, ModelIntegrityError

GOLD = 1
SILVER = 2
COPPER = 3



class Money():
    def __init__(self, id=None, player_id=None, code=None, amount=None, created=None, updated=None):
        self.id = id
        self.player_id = player_id
        self.code = code
        self.amount = amount
        self.created = created
        self.updated = updated

    def as_dict(self):
        d = {
            "id" : self.id,
            "player_id" : self.player_id,
            "code":self.code,
            "amount":self.amount,
            "created" : self.created,
            "updated" : self.updated,
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.id = object_as_dict["id"]
        self.player_id = object_as_dict["player_id"]
        self.code = object_as_dict["code"]
        self.amount = object_as_dict["amount"]
        self.created = object_as_dict["created"]
        self.updated = object_as_dict["updated"]
        return object_as_dict

    def load_from_db(self, player_id):
        """
            Method for loading player instance from DB row
            :param email: Player email for loading all info from db
            :return: None
        """

        cursor = connection.cursor()

        sql_query = """SELECT id, player_id, code, amount, created, updated
                       FROM Money WHERE player_id=%(player_id)s"""

        sql_args = {
            "player_id": player_id
        }

        new_list = []

        cursor.execute(sql_query, sql_args)
        db_row = cursor.fetchone()
        for elem in db_row:
            new_list.append(elem)

        print u"\n################################\n" \
              u"ID        : {}\n" \
              u"Player_id : {}\n" \
              u"Code      : {}\n" \
              u"Amount    : {}\n" \
              u"Created   : {}\n" \
              u"Updated   : {}\n" \
              u"################################\n" \
              u"Was loaded from db.\n".format(new_list[0], new_list[1], new_list[2], new_list[3],
                                              new_list[4], new_list[5])

        self.id = db_row[0]
        self.player_id = db_row[1]
        self.code = db_row[2]
        self.amount = db_row[3]
        self.created = db_row[4]
        self.updated = db_row[5]

    def save_to_db(self):
        """
            Save all player data to MySQL database.
            If a record with player is not exists, it is inserted.
            If method knows _id of player, it will try to update existing
            db record.

            :return: None
        """
        insert_query = """INSERT INTO Money (player_id, code, amount, created, updated)
                          VALUES (%(player_id)s, %(code)s, %(amount)s,  now(), now())"""

        update_query = """UPDATE Money SET  code=%(code)s, amount=%(amount)s, updated=now() WHERE player_id=%(player_id)s"""

        sql_data = {
            "player_id": self.player_id,
            "code": self.code,
            "amount": self.amount,
        }

        cursor = connection.cursor()
        if self.id is None:
            try:
                cursor.execute(insert_query, sql_data)
                self.id = cursor.lastrowid  # cursor.fetchone()[0]
            except ModelIntegrityError:
                print("\nDEBUG: an integrity error occured when session inserting, it's OK")
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
        delete_query = "DELETE FROM Money WHERE id=%(id)s"
        sql_data = {
            "id": self.id
        }
        cursor.execute(delete_query, sql_data)

    def __str__(self):
        return u"\n#########################################\n" \
               u'ID         : {};\n' \
               u'Player_id  : {};\n' \
               u'Code       : {};\n' \
               u'Amount     : {};\n' \
               u'Created    : {};\n' \
               u'Updated    : {};\n' \
               u"#########################################\n" \
               .format(self.id, self.player_id, self.code, self.amount,self.created, self.updated)



class Wallet():
    def __init__(self, gold, silver, copper):

        if gold.code != GOLD:
            raise Exception("gold.code != GOLD")
        if silver.code != SILVER:
            raise Exception("silver.code != SILVER")
        if copper.code != COPPER:
            raise Exception("copper.code != COPPER")

        self.gold   = gold
        self.silver = silver
        self.copper = copper
        self.money = {
        GOLD:   gold,
        SILVER: silver,
        COPPER: copper
        }

    def as_dict(self):
        d = {
            "gold":self.gold.as_dict(),
            "silver":self.silver.as_dict(),
            "copper":self.copper.as_dict()
            }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.gold =   object_as_dict["gold"]
        self.silver = object_as_dict["silver"]
        self.copper = object_as_dict["copper"]
        return object_as_dict

    def load_from_db(self, player_id):
        """
            Method for loading player instance from DB row
            :param email: Player email for loading all info from db
            :return: None
        """

        cursor = connection.cursor()

        sql_query = """SELECT id, player_id, start_time, finish_time, elapse_time, created, updated
                       FROM Session WHERE player_id=%(player_id)s"""

        sql_args = {
            "player_id": player_id
        }

        new_list = []

        cursor.execute(sql_query, sql_args)
        db_row = cursor.fetchone()
        for elem in db_row:
            new_list.append(elem)

        print u"\n#################################\n" \
              u"ID          : {}\n" \
              u"Player_id   : {}\n" \
              u"Start_time  : {}\n" \
              u"Finish_time : {}\n" \
              u"Elapse_time : {}\n" \
              u"Created     : {}\n" \
              u"Updated     : {}\n" \
              u"#################################\n" \
              u"Was loaded from db.\n".format(new_list[0], new_list[1], new_list[2], new_list[3],
                                              new_list[4], new_list[5], new_list[6])

        self.id = db_row[0]
        self.player_id = db_row[1]
        self.start_time = db_row[2]
        self.finish_time = db_row[3]
        self.elapse_time = db_row[4]
        self.created = db_row[5]
        self.updated = db_row[6]

    def __str__(self):
        return u'Gold   - {};' \
               u'\n           Silver - {};' \
               u'\n           Copper - {};'.format(self.gold, self.silver, self.copper)