# -*- coding: utf-8 -*-
import json
import sys
import datetime
import MySQLdb

from connection_db  import connection, ModelIntegrityError


class Session():
    def __init__(self,  id=None,            player_id=None,  start_time=datetime.datetime.now(), finish_time=None,
                        elapse_time=None,   created=None,    updated=None):
        self.id = id
        self.player_id = player_id
        self.start_time = start_time
        self.finish_time = finish_time
        self.elapse_time = elapse_time
        self.created = created
        self.updated = updated

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
                elapsedTime = (self.end_time) -\
                              (self.start_time)
        else:
            # Timer hasn't started, error on the side of caution
            rightNow = datetime.datetime.now()
            elapsedTime = (rightNow - rightNow)
        return(elapsedTime)


    def as_dict(self):
        d = {
            "id" :self.id,
            "player_id" :self.player_id,
            "start_time":self.start_time,
            "end_time":self.end_time,
            "elapse_time" :self.elapse_time,
            "created" :self.created,
            "updated" : self.updated,
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.id = object_as_dict["id"]
        self.player_id = object_as_dict["player_id"]
        self.start_time = object_as_dict["start_time"]
        self.finish_time = object_as_dict["finish_time"]
        self.elapse_time = object_as_dict["elapse_time"]
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

    def save_to_db(self):
        """
            Save all player data to MySQL database.
            If a record with player is not exists, it is inserted.
            If method knows _id of player, it will try to update existing
            db record.

            :return: None
        """
        insert_query = """INSERT INTO Session (player_id, start_time, finish_time, elapse_time, created, updated)
                          VALUES (%(player_id)s, %(start_time)s, %(finish_time)s, %(elapse_time)s, now(), now())"""

        update_query = """UPDATE Session SET  start_time=%(start_time)s, finish_time=%(finish_time)s,
                                              elapse_time=%(elapse_time)s, updated=now() WHERE player_id=%(player_id)s"""


        sql_data = {
            "player_id": self.player_id,
            "start_time": self.start_time,
            "finish_time": self.finish_time,
            "elapse_time": self.elapse_time,
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
        delete_query = "DELETE FROM Session WHERE id=%(id)s"
        sql_data = {
            "id": self.id
        }
        cursor.execute(delete_query, sql_data)

    def __str__(self):
        return u"\n#########################################\n" \
               u'ID          : {};\n' \
               u'Player_id   : {};\n' \
               u'Start_time  : {};\n' \
               u'Finish_time : {};\n' \
               u'Elapse_time : {};\n' \
               u'Created     : {};\n' \
               u'Updated     : {};\n' \
               u"#########################################\n" \
               .format(self.id, self.player_id, self.start_time, self.finish_time,
                    self.elapse_time, self.created, self.updated)
