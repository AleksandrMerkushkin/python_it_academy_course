import MySQLdb

con = MySQLdb.connect('localhost', 'root', 'd6d5bd92', 'game_admin');

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Player")
    for row in cur.fetchall():
        print row
