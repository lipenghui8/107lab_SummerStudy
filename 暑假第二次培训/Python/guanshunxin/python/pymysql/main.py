#1导包
import pymysql
#2链接
connc=pymysql.Connect(
    #mysql 服务端ip
    user='root',
    password='123456',
    database='person',
    charset='utf8'
)
#3创建游标对象
cur=connc.cursor()
#4编写sql
# sql='select * from infomation;'
# #5使用游标对象调SQL
# cur.execute(sql)
# #6获取查询结结果
# result=cur.fetchall()
# print(result)
# #7关闭游标对象
# cur.close()
# connc.close()
#增加对象
# sql='insert into infomation values(%s,%s,%s,%s)'
# add_data=[0,'刘德华',66,'男']
# cur.execute(sql,add_data)
# connc.commit()
# cur.close()
# connc.close()
#修改
# sql='update infomation set name=%s where name="老王"'
# update_data=['老王八']
# cur.execute(sql,update_data)
# connc.commit()
# cur.close()
# connc.close()
#删除
try:
    sql='delete from infomation where name=%s'
    del_data=['来了']
    cur.execute(sql,del_data)
    connc.commit()
except Exception as e:
    print(e)
    #数据回滚
    connc.rollback()
finally:
    cur.close()
    connc.close()
