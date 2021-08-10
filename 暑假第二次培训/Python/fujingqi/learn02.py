# 增加数据
# 加入kyrie的个人信息

import pymysql

connc = pymysql.Connect(
            host='101.34.91.225',
            user='107lab_2021',
            password="107lab_2021_six",
            database='107lab_2021',
            port=3306,
            charset='utf8'
)

cur = connc.cursor()

sql = 'insert into Fujingqi values(%s, %s, %s, %s, %s, %s)'
add_data = [0, 'kyrie', 25, 'male', 78.9, 'paid']

cur.execute(sql, add_data)

connc.commit()

cur.close()

connc.close()
