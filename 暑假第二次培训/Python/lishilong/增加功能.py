import pymysql
connc = pymysql.connect(
    host='101.34.91.225',
    user='107lab_2021',
    password='107lab_2021_six',
    database='107lab_2021',
    port=3306,
    charset='utf8'
)
#数据库的增加功能
cur = connc.cursor()
sql = 'insert into lishilong values(%s,%s,%s,%s,%s,%s,%s)'
data = [5, '10', '10', '10', '张三', '待收货', '2020-04-12']
cur.execute(sql, data)
connc.commit()
cur.close()
connc.close()