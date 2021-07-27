# 数据查询

# 导包
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

# 创建游标对象
cur = connc.cursor()

# 编写SQL语句(查询)
sql = 'select * from chenlimin;'

# 使用游标对象去调用SQL
cur.execute(sql)

# 获取查询结果，并输出
res = cur.fetchall()
print(res)

# 关闭游标对象
cur.close()
# 关闭链接
connc.close()
