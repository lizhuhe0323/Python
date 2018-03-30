import pymysql

def select(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='pycharm')
    cur = conn.cursor()
    cur.execute("select password from user where username=%s",args=user)
    for r in cur.fetchall():
        return("".join(r))
    cur.close()
    conn.close()

def insert(username,password):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='pycharm')
    cur = conn.cursor()
    cur.executemany("insert into user(username,password) values(%s,%s)", [(username,password)])
    conn.commit()
    cur.close()
    conn.close()