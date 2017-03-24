import MySQLdb
from _mysql import IntegrityError



ModelIntegrityError = IntegrityError
connection = MySQLdb.connect(host='localhost', user='root', passwd='root',
                             db='game_admin', autocommit=True)
