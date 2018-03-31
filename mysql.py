import pymysql

def select(user):
    try:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='pycharm')
        cur = conn.cursor()
        cur.execute("select password from user where username=%s",args=user)
        for r in cur.fetchall():
            return("".join(r))
        cur.close()
        conn.close()
    except (ConnectionError,ConnectionRefusedError,ConnectionResetError):
        print ("\033[0;33m%s\033[0m" % "Database connect error!")
        pass

def insert(username,password):
    try:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='pycharm')
        cur = conn.cursor()
        cur.executemany("insert into user(username,password) values(%s,%s)", [(username,password)])
        conn.commit()
        cur.close()
        conn.close()
    except (ConnectionError,ConnectionRefusedError,ConnectionResetError):
        print ("\033[0;33m%s\033[0m" % "Database connect error!")
        pass