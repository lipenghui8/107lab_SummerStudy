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

#删除数据
sql = 'delete from likunsong where user=%s'
del_data = ['李磊']
#5.使用游标对象去调用SQL

cur.execute(sql)
# 提交
connnc.commit()
#7.关闭游标对象

cur.close()
#8.关闭连接
connnc.close()