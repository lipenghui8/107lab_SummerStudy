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

#4.增加
sql = 'insert into likunsong values(%s,%s,%s,%s,%s,%s,%s)'
add_data1 = [0, 2, 100.00 , 10.00 , '老王', '待收货', '2021-01-01']
add_data2 = [0,3,200.00,25.00,'钱红','待支付','2021-03-04']
add_date5 = [0 , 1 , 99.00 , 9.00 , '小丽' , '待收货' , '2021-4-12']
add_data4 = [0,5,50.00,20.00,'李湘','待发货','2021-4-17']

# 添加信息
cur.execute(sql,add_data1)
cur.execute(sql,add_data2)
cur.execute(sql,add_date5)
cur.execute(sql,add_data4)
# 提交
connnc.commit()
#关闭游标对象
cur.close()
#8.关闭连接
connnc.close()