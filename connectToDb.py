import pymysql.cursors


# Connect to the database
def connectToDB():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='salmanwholeseller',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
