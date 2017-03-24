import MySQLdb
import sys

try:
    db = MySQLdb.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            db = 'game_admin'
            )

except Exception as e:
    sys.exit('We cant get into the datebase')

with db:
    cursor = db.cursor()
    # cursor.execute("UPDATE Player SET email='vasya@vasya.com' WHERE nickname='Vasya';")
    # cursor.execute("UPDATE Player SET password='abc123new', nickname='Vasya_new'  WHERE id=1;")
    cursor.execute("INSERT INTO `player`(`type`, `nickname`, `email`, `password`, `created`, `updated`) VALUES (0, 'admin_Vasya3', 'vasya_admin3@tut.by', 'abc1234567', now(), now());")
    cursor.execute("SELECT * FROM player")
    result = cursor.fetchall()

    if result:
        for row in result:
            print u"id       : {}\n" \
                  u"type     : {} (admin=0, user=1)\n" \
                  u"nickname : {}\n" \
                  u"email    : {}\n" \
                  u"password : {}\n" \
                  u"created  : {}\n" \
                  u"updated  : {}\n".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6])