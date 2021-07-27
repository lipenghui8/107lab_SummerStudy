# 删除对象

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

# 编写SQL语句（删除）
sql = 'delete from chenlimin where count=%s'
del_data = [3]

# 使用游标对象去调用SQL
cur.execute(sql, del_data)

# 提交数据库
connc.commit()

# 关闭游标对象
cur.close()
# 关闭链接
connc.close()
