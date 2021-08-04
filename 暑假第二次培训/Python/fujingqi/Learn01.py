# 数据查询

# 导包
import pymysql

# 连接mysql数据库的服务
connc = pymysql.Connect(
            host='101.34.91.225',               # mysql服务端的IP 默认127.0.0.1//localhost-真实IP
            user='107lab_2021',                 # 用户名
            password="107lab_2021_six",         # 密码
            database='107lab_2021',            #
            port=3306,
            charset='utf8'
)

cur = connc.cursor()

sql = 'select * from Fujingqi;'

cur.execute(sql)

res = cur.fetchall()
print(res)

cur.close()

connc.close()
