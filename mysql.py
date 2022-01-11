import pymysql


def getdata(sql):
    db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", db="bookstoredb")
    cursor = db.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    db.close()
    return datas


if __name__ == '__main__':
    # sql = "select * from user"
    sql2 = "CREATE DATABASE bookstoredb;"
    # data = getdata(sql)
    data2 = getdata(sql2)
    print(data)
    for i in data:
        print(i)
    print(data2)