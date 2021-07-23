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
#4.编写SQL语句
# 查询所有likunsong表里面的数据
sql = 'select * from likunsong'


#5.使用游标对象去调用SQL

cur.execute(sql)


#6.获取查询结果  -- print（） 提交操作
result = cur.fetchall()

# 将数据转换成[{},{}]
data_list = []
for row in result:
    data_list.append({
        'id' : row[0],
        'count' : row[1],
        'price' : str(row[2]),
        'freight' : str(row[3]),
        'user' : row[4],
        'status' : row[5],
        'time' : str(row[6]),
    })

print('查询',data_list)

#7.关闭游标对象

json_str = json.dumps(data_list , ensure_ascii=False)

cur.close()
#8.关闭连接
connnc.close()