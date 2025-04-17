import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost", user="tester", password="whdwls212@", database="test"
)

# mycursor = mydb.cursor()
now = datetime.now()
# #########################insert

# sql = "INSERT INTO user (name, age, create_date_time, update_date_time) VALUES (%s, %s, %s, %s)"
# val = ("강감찬", 35, now, now)
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# #########################select

# 커서에 옵션으로 dictionary=True를 주면 컬럼명과 데이터값이 dictionary형태로 나옴
# mycursor = mydb.cursor(dictionary=True)
# sql = "select * from user"
# mycursor.execute(sql)
# # fetchall() : 전부 다 가져옴. fetchone() : 하나만 가져옴.
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# print(myresult[0]["name"])


mycursor = mydb.cursor(dictionary=True)

# ####################### 한 결과만 select
# sql = "select * from user where id = 5"
# mycursor.execute(sql)
# # fetchall() : 전부 다 가져옴. 리스트로 감싸져 있어 번지수로 번저 찾아야함.
# # fetchone() : 하나만 가져옴. 리스트가 아닌 한 row만 가져옴
# myresult = mycursor.fetchone()

# print(myresult["name"], myresult["age"])

# sql = "select * from user where age = %s"
# val = (35,)

# mycursor.execute(sql, val)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# 정렬

# sql = "select * from user order by name desc"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

sql = "delete from user where name = %s"
val = ("홍길동",)
mycursor.execute(sql, val)
mydb.commit()


mydb.close()
