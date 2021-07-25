#1.导包

import pymysql
#链接数据库
connc = pymysql.Connect(
        host='192.168.3.20',
        user='root',
        password="0159",
        database='orders',
        port=3306,
        charset='utf8'
)

#3创建游标对象
cur = connc.cursor()


try:
        #4编写 查询orders表的所有数据sql
        sql='select * from beijiayang;'

        #5.使用游标对象执行sql
        cur.execute(sql)

        #6 .获取查询的所有结果
        result=cur.fetchall()
        print("查询数据：",result)

        #try的优化
except Exception as  e:
        print('报错信息：',e)
finally:
        cur.close()

        connc.close()

print('game over')