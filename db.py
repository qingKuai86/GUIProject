import pymysql
Username=""
def conn():#连接数据库
    db = pymysql.connect(host="localhost", user="root", password="123456", database="stu", charset='utf8')
    return db
def update(sql,*values):#shift键，单tab
    db1=conn()
    cursor1 = db1.cursor()
    try:
        cursor1.execute(sql,values)
        db1.commit()
        return 1
    except:
        db1.rollback()
        return 0
    finally:
        cursor1.close()
        db1.close()
def update2(sql):#shift键，单tab
    db1=conn()
    cursor1 = db1.cursor()
    try:
        cursor1.execute(sql)
        db1.commit()
        return 1
    except:
        db1.rollback()
        return 0
    finally:
        cursor1.close()
        db1.close()
def query(sql,*keys):
    db2=conn()
    cursor2=db2.cursor()
    cursor2.execute(sql,keys)
    rs=cursor2.fetchall()
    cursor2.close()
    db2.close()
    return rs
def query2(sql):
    db3=conn()
    cursor3=db3.cursor()
    cursor3.execute(sql)
    rs=cursor3.fetchall()
    row=cursor3.rowcount
    cursor3.close()
    db3.close()
    return rs,row