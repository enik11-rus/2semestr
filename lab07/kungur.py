
import pymysql.cursors

conn = pymysql.connect(
    host='pgsha.ru',
    user='soft0046',
    password='vCDRap4A',
    db='soft0046_labrab',
    port=35006,
    cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

sql = "SElECT * FROM students WHERE city = Кунгур"
cur.execute(sql)
rows = cur.fetchall()

print(rows)

conn.close()