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

sql = 'update xuecheng set name = %s where name = "老王"'
update_data = ['xiaowang']

cur.execute(sql, update_data)

connc.commit()

cur.close()

connc.close()