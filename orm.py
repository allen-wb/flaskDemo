from sqlalchemy import create_engine
from sqlalchemy import String, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'  # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


#  初始化数据库连接:
engine = create_engine('mysql+pymysql://root:admin@192.168.1.51:3306/wb_test?charset=utf8', echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


