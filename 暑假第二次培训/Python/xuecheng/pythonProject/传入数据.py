#1.导包
import json

import pymysql
#2.连接数据库
connnc = pymysql.Connect(
        host='101.34.91.225',
# mysql服务端的IP 默认的是127.0.0.1，这个是localhost的真实IP
        user='107lab_2021',
        password="107lab_2021_six",
        database="107lab_2021",
        port=3306,
        charset='utf8'
    )
    # 3.创建游标对象
    cur = connnc.cursor()

#插入的信息
sql = 'insert into xuecheng values(%s,%s,%s,%s,%s,%s,%s)'
add_data1 = [1, 2, 100.00, 10.00, '老王', '待收货', '2021-01-01']
add_data2 = [2,3,200.00,25.00,'钱红','待支付','2021-03-04']
add_data3 = [3,1,99.00,9.00,'小丽','待收货','2021-01-01']
add_data4 = [4,5,10.10,10.00,'李响','待发货','2021-02-08']
add_data5 = [5,6,600.00,18.00,'张华','待支付','2021-02-03']
add_data6 = [6,8,88.00,57.00,'laowang','待发货','2021-10-16']

#添加信息
cur.execute(sql,add_data1)
cur.execute(sql,add_data2)
cur.execute(sql,add_data3)
cur.execute(sql,add_data4)
cur.execute(sql,add_data5)
cur.execute(sql,add_data6)

try:
    cur.execute(sql, data)
    connnc.commit()
except Exception as e:
    print('操作失败：', e)
    # 回滚数据
    connnc.rollback()
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    connnc.close()