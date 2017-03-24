import mysql.connector



def connect():
    """ Connect to MySQL database """
    config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'game_admin',
            # 'raise_on_warnings': True,
            # 'use_pure': False,
            }
    try:
        print('Connecting to MySQL database...')
        cnx = mysql.connector.connect(**config)
        cnx.set_autocommit(True)

        if cnx.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as e:
        print(e)

    finally:
        cnx.close()
        print('Connection closed.')

if __name__ == '__main__':
    connect()