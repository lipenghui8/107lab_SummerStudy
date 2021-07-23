#1.导包
import json

import pymysql
#2.连接MySQL数据库的服务
connnc = pymysql.Connect(
    host='101.34.91.225',
    user='107lab_2021',
    password="107lab_2021_six",
    database="107lab_2021",
    port=3306,
    charset='utf8'
)
#3.创建游标对象
cur = connnc.cursor()

#4.修改
sql = 'update likunsong user set user=%s where user="Lily"'
update_data = ['lisa']

#5.使用游标对象调用sql
cur.execute(sql , update_data)
# 6.提交
connnc.commit()
#7.关闭游标对象

cur.close()
#8.关闭连接
connnc.close()