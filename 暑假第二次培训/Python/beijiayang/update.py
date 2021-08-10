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
        #4编写 增加表的所有数据sql
        sql='update beijiayang set  age=22，name=maniubi where id=4;'

        #5.使用游标对象执行sql
        cur.execute(sql,body)

        #6 .提交操作
        connc.commit()

        #try的优化
except Exception as  e:
        print('操作失败：',e)
finally:
        cur.close()

        connc.close()

print('game over')