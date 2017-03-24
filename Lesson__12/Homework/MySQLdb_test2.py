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

sql_data = {
    "id": 1,
    "code": 3,
    "amount": 1000,
}

sql_query = """UPDATE Money SET amount=amount+%(amount)s WHERE player_id=%(id)s AND
               code=%(code)s"""
with db:
    cursor = db.cursor()
    cursor.execute(sql_query, sql_data)
    cursor.execute("SELECT * FROM Money")

    result = cursor.fetchall()

    for row in result:
        print u"id          : {}\n" \
              u"player_id   : {}\n" \
              u"code        : {} (Gold=1, Silver=2, Copper=3)\n" \
              u"amount      : {}\n" \
              u"created     : {}\n" \
              u"updated     : {}\n".format(row[0],row[1],row[2],row[3],row[4],row[5])
