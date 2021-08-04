import pymysql
connc = pymysql.connect(
    host='101.34.91.225',
    user='107lab_2021',
    password='107lab_2021_six',
    database='107lab_2021',
    port=3306,
    charset='utf8'
)
#数据库的查询功能
cur = connc.cursor()
sql = 'select * from lishilong;'
cur.execute(sql)
result = cur.fetchall()
datalist = []
for row in result:
    datalist.append({
        'id': row[0],
        'count': row[1],
        'price': str(row[2]),
        'freight': str(row[3]),
        'user': row[4],
        'status': row[5],
        'time': str(row[6]),
    })
print("数据查询：", datalist)
cur.close()
connc.close()




