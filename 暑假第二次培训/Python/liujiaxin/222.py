import pymysql

connc = pymysql.Connect(
    host='101.34.91.225',
    user='107lab_2021',
    password="107lab_2021_six",
    database='107lab_2021',
    port=3306,
    charset='utf8'
)

cur = connc.cursor()

sql = 'insert into liujiaxin values(%s,%s,%s,%s,%s)'
sql1 = 'update liujiaxin set name=%s where name="ljx"'
sql2 = 'delete from liujiaxin where name=%s'
add_data = [0, 'zam', 'male', 19, 'paid']
update_data = ['ljxdsg']
del_data = ['cts']

cur.execute(sql, add_data)

cur.execute(sql1, update_data)

cur.execute(sql2, del_data)

connc.commit()

cur.close()

connc.close()
