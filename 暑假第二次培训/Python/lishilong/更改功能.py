import pymysql
connc = pymysql.connect(
    host='101.34.91.225',
    user='107lab_2021',
    password='107lab_2021_six',
    database='107lab_2021',
    port=3306,
    charset='utf8'
)
#数据库的更改功能
cur = connc.cursor()
sql = 'update lishilong set user="钱红" where id=2'
cur.execute(sql)
connc.commit()
cur.close()
connc.close()