import pymysql.cursors


# Connect to the database
def connectToDB():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456789Aa@',
                                 db='mysql',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
