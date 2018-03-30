import cx_Oracle

# 建立和数据库系统的连接
conn = cx_Oracle.connect('emssxjk/emssxjk@orcl')
# 获取操作游标
cursor = conn.cursor()
# 执行SQL,创建一个表
cursor.execute("""create table tb_user(id number, name varchar2(50),password varchar(50),primary key(id))""")
# 关闭连接，释放资源
cursor.close()
# 执行完成，打印提示信息
print ('Completed!')

# 插入一条记录
cursor.execute("""insert into tb_user values(1,'admin','password')""");

# 再插入一条数据
param = {'id': 2, 'n': 'admin', 'p': 'password'}
cursor.execute('insert into tb_user values(:id,:n,:p)', param);

# 一次插入多条数据,参数为字典列表形式
param = [{'id': 3, 'n': 'admin', 'p': 'password'}, {'id': 4, 'n': 'admin', 'p': 'password'},
         {'id': 5, 'n': 'admin', 'p': 'password'}];
cursor.executemany('insert into tb_user values(:id,:n,:p)', param);

# 再一次插入多条数据
param = [];
# 生成5条插入数据，参数为元组列表形式
for i in range(6, 11):  # [6,7,8,9,10]
    param.append((i, 'user' + str(i), 'password' + str(i)))
# 插入数据
cursor.executemany('insert into tb_user values(:1,:2,:3)', param);

cursor.close();
# 提交更改
conn.commit();
conn.close();

# 执行查询 语句
cursor.execute("""select * from tb_user""")

# 获取一条记录
one = cursor.fetchone()
print ('1: id:%s,name:%s,password:%s' % one;)

# 获取两条记录!!!注意游标已经到了第二条
two = cursor.fetchmany(2)
print ('2 and 3:', two[0], two[1])

# 获取其余记录!!!注意游标已经到了第四条
three = cursor.fetchall();
for row in three:
    print (row)  # 打印所有结果

print （'条件查询'）
cursor.prepare("""select * from tb_user where id <= :id""")
cursor.execute(None, {'id': 5})
for row in cursor:  # 相当于fetchall()
    print （row）

cursor.close();
conn.close();