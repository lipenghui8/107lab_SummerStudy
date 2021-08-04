#1.导包
import pymysql

# 连接mysql数据库的服务
connc = pymysql.Connect(
            host='101.34.91.225',
            user='107lab_2021',
            password="107lab_2021_six",
            database='107lab_2021',
            port=3306,
            charset='utf8'
)

cur = connc.cursor()

sql = 'select * from Fujingqi;'

cur.execute(sql)

result = cur.fetchall()
print(result)

cur.close()