from sqlalchemy import create_engine
from sqlalchemy import String, Column, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'  # 表的结构
    id = Column(String(32), primary_key=True)
    name = Column(String(20))
    password = Column(String(20))
    sex = Column(Integer)
    email = Column(String(20))
    create_time = Column(DateTime)


class Blog(Base):
    __tablename__ = 'blog'
    id = Column(String(32), primary_key=True)
    user_id = Column(String(32))
    user_name = Column(String(20))
    name = Column(String(20))
    summary = Column(String(200))
    content = Column(String(900))
    create_at = Column(DateTime)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(String(32), primary_key=True)
    blog_id = Column(String(32))
    user_id = Column(String(32))
    user_name = Column(String(20))
    content = Column(String(900))
    create_at = Column(DateTime)


#  初始化数据库连接:
engine = create_engine('mysql+pymysql://root:admin@192.168.1.51:3306/wb_test?charset=utf8', echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


