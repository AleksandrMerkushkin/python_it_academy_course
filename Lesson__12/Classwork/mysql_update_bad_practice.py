
import MySQLdb

con = MySQLdb.connect('localhost', 'root', 'd6d5bd92', 'game_admin');

sql_data = {
    "id": 1,
    "code": 3,
    "amount": 1000,
}
sql_query = """UPDATE Money SET amount=amount+%(amount)s WHERE player_id=%(id)s AND
               code='%(code)s'"""

sql_query = sql_query % sql_data

with con:
    cur = con.cursor()
    cur.execute(sql_query)

    cur.execute("SELECT * FROM Money")
    for row in cur.fetchall():
        print row