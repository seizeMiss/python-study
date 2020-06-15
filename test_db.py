import pymysql as conn

#  打开数据库链接
db = conn.connect('localhost', 'root', 'root', 'wallet')
#  使用cursor() 方法创建已给游标对象cursor
cursor = db.cursor()
#  执行execut()方法执行sql查询
cursor.execute('SELECT version()')

#  使用fetchone方法获取单条数据
data = cursor.fetchone()

print('Database version:%s' % data)

#  关闭数据库
db.close()