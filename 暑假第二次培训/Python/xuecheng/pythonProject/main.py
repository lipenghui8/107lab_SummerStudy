import json

import pymysql


#封装一个函数
def execut_crud_sql(sql,data):
    # 2.连接mysql数据库的服务
    connnc = pymysql.Connect(
        host='101.34.91.225',
        user='107lab_2021',
        password="107lab_2021_six",
        database="107lab_2021",
        port=3306,
        charset='utf8'
    )
    # 3.创建游标对象
    cur = connnc.cursor()

    try:
        cur.execute(sql,data)
        connnc.commit()
    except Exception as e:
        print('操作失败：',e)
        #回滚数据
        connnc.rollback()
    finally:
        #关闭游标
        cur.close()
        #关闭连接
        connnc.close()

#显示信息
def order(body):
    connnc = pymysql.Connect(
        host='101.34.91.225',
        user='107lab_2021',
        password="107lab_2021_six",
        database="107lab_2021",
        port=3306,
        charset='utf8'
    )
    # 3.创建游标对象
    cur = connnc.cursor()
    try:
        sql = 'select * from xuecheng;'
        cur.execute(sql)
        #获取查询的所有结果
        result = cur.fetchall()
        #将数据转换成【{}，{}】
        data_list = []
        for row in result:
            data_list.append({
                'id': row[0],
                'count': row[1],
                'price': str(row[2]),
                'freight': str(row[3]),
                'user': row[4],
                'status': row[5],
                'time': str(row[6]),
            })
    except Exception as e:
        print('报错信息：',e)
    finally:
        cur.close()
        connnc.close()

#增加订单数据
def add(body):
    sql = 'insert into xuecheng values(%s,%s,%s,%s,%s,%s,%s)'
    execut_crud_sql(sql,body)

#修改信息
def updata(body):
    sql = 'update xuecheng neme set count=%s,price=%s,freight=%s,status=%s,time=%s where id=%s'
    execut_crud_sql(sql,body)

#删除信息
def delete(body):
    sql = 'delete from xuecheng where id = %s'
    execut_crud_sql(sql,body)









