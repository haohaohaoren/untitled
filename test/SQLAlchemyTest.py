#coding:utf8
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  *
from sqlalchemy.orm import  *
from sqlalchemy import MetaData
from sqlalchemy.sql import *
def createEngine():
    #useUnicode=true&characterEncoding=UTF-8   charset=utf8
    engine = create_engine("mysql://root:wuhao123@192.168.1.17/test?charset=utf8", encoding='utf8', echo=True,
                           convert_unicode=True)
    return engine
def createSQliteEngine():
     engine = create_engine(r"sqlite:///mydata.db",echo=False)
#创建表方式1
def method1():
    # engine =create_engine("sqlite:////C:\\Users\\wuhaohao\\PycharmProjects\\untitled\\test\\mydata.db",echo=False) #:memory:
    # mysql连接没有问题
    engine = createEngine()

    # engine =create_engine(r"sqlite:////:memory:",echo=False)
    Base = declarative_base()

    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(255))
        fullname = Column(String(255))
        password = Column(String(255))

        def __repr__(self):
            return "<User(name ='%s',password ='%s'" % (self.name, self.password)

    # Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(name='浩3', fullname='武浩3', password='haoha1o')
    # session.add(user)
    # session.commit()
    allusers = session.query(User).all()
    for u in allusers:
        print u.id, u.name, u.fullname, u.password
#创建表方式1

def  method2():

     engine = createEngine()
     metadata =MetaData(engine)
     user = createTableUser(metadata)
     metadata.create_all(engine)
     conn = engine.connect()
     i = user.insert()
     u =dict(name='浩001',fullname ="好好",password="123344adf")
     r1 = conn.execute(i,**u)
     print r1.inserted_primary_key

     #############一.以每次插入一条记录的方式向user表插入数据##############
     # 使用查询
     #i = user.insert()
     # print i
     # 插入一组数据
     #u = dict(name='tom', fullname='tom smith')  # id从1自动增加
     # 执行查询，第一个为查询对象，第二个参数为一个插入数据字典，如果插入的是多个对象
     # 就把对象字典放在列表里边
     #r1 = conn.execute(i, **u)
     # print r1
     # 返回插入行
     #print r1.inserted_primary_key
     ############二.以每次插入多条记录的方式向address表插入数据#############
    # addr = [{'user_id': 1, 'email': 'jack@yahoo.com'}, {'user_id': 1,
      #                                                   'email': 'jack@msn.com'},
     #        {'user_id': 2, 'email': 'www@www.org'},
     #        {'user_id': 2, 'email': 'wendy@aol.com'}]
    # j = address.insert()
    # r2 = conn.execute(j, addr)
#创建user表
def createTableUser(metadata):
    user = Table('users', metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('name', String(20), nullable=False),
                 Column('fullname', String(100), nullable=False),
                 Column('password', String(100), nullable=False)
                 )
   # __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    return user
#check users
def method3():
    engine =createEngine()
    metadata =MetaData(engine)
    user = createTableUser(metadata)
    #metadata.create_all(engine)
    conn = engine.connect()
    #原生态sql方式
    #s =text("select users.id,users.name from users where users.id =:id")
    s = text("select users.id,users.name from users")
    print s
    s1 = select([user.c.id,user.c.name,user.c.fullname]).where(user.c.id>5) #查询全表
    #执行查询不使用fatch的方式 1
    for u in conn.execute(s,id=3):
        print u[0],u[1]

    #print(s1)
    r1 =conn.execute(s1) #执行查询
    #执行查询使用 fatch的方式  2
    # 返回查询结果!!!!!
    # 只要 r.fetchall() 之后，就会自动关闭 ResultProxy 对象
    for u in r1.fetchall():
        #print u
         pass
    # user.c表 user 的字段column对象
    s2 = select([user.c.name, user.c.fullname])  # 查询部分
    # 功能：实现同时对两个表的查询
    #s = select([user.c.name, address.c.user_id]).where(user.c.id == address.c.user_id)

def createTableOnSqlite():
    engine = createTableOnSqlite()
    metadata = MetaData(engine)
    createTableUser()
    metadata.create_all(engine)
def insertDataSqlite():
    pass
#SQLALchemy 使用sqlite数据库
def checkDataSqlite():
     engine = createSQliteEngine()
     metadata = MetaData(engine)
     user = createTableUser(metadata)
     conn = engine.connect()
     # 原生态sql方式
     s = text("select users.id,users.name from users where users.id =:id")
     print s
     # 执行查询不使用fatch的方式 1
     for u in conn.execute(s, id=3):
         print u[0], u[1]
#插入数据
def insertDataMysql():
    engine = createEngine()
    metadata =MetaData(engine)
    user = createTableUser(metadata)
    conn =engine.connect()
    u =dict(name='浩浩',fullname = '武好好',password ='qwaszx2')
    i =user.insert()
    conn.execute(i,u)



if __name__ =='__main__':
    #method2()
    #insertDataMysql()
    method3()
   # checkDataSqlite()


