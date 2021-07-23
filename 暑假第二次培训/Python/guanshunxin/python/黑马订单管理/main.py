#1导包
import pymysql
#2链接
connc=pymysql.Connect(
    #mysql 服务端ip
    host='101.34.91.225',
    user='107lab_2021',
    password='107lab_2021_six',
    database='107lab_2021',
    port=3306,
    charset='utf8'
)
#3创建游标对象
cur=connc.cursor()
# try:
#     sql='select * from guanshunxin;'
#     cur.execute(sql)
#     result=cur.fetchall()
#     # print(result)
#     data_list=[]
#     for row in result:
#         data_list.append({
#             'id':row[0],
#             'count': row[1],
#             'price': str(row[2]),
#             'freight': str(row[3]),
#             'user': row[4],
#             'status': row[5],
#             'time': str(row[6]),
#         })
# except Exception as e:
#     print(e)
# finally:
#     cur.close()
#     connc.close()
#print(data_list)
# sql='insert into guanshunxin values(%s,%s,%s,%s,%s,%s)'
# add_data=[0,'刘德华',66,'男']
# cur.execute(sql,add_data)
# connc.commit()
# cur.close()
# connc.close()