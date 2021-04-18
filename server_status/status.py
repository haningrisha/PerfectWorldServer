from mysql.connector import errorcode
import mysql.connector

if __name__ == '__main__':
    try:
        cnx = mysql.connector.connect(user='root', passwd='server2021',
                                      host='45.90.46.29', port='31001')
    except mysql.connector.errorcode as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
