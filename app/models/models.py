# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base  # 模型继承的父类
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, CHAR, DATETIME  # mysql字段类型
from sqlalchemy import Column  # 指定字段类

Base = declarative_base()
metadata = Base.metadata
# 1.短网址信息表
"""
设计字段
1.编号：id，主键，自动递增，大整型
2.原始网址：url，唯一，非空，变长字符串类型
3.缩短码：code，唯一，非空，定长字符串类型
4.唯一标识符：uuid，唯一，非空，定长字符串类型
5.创建时间：createdAt，非空，日期时间类型
6.修改时间：updatedAt，非空，日期时间类型
"""


# 短网址信息模型
class ShortUrl(Base):
    __tablename__ = "shorturl"
    id = Column(BIGINT, primary_key=True)
    url = Column(VARCHAR(255), unique=True, nullable=False)
    code = Column(CHAR(8), unique=True, nullable=False)
    uuid = Column(CHAR(32), unique=True, nullable=False)
    createdAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)


# 2.短网址统计表
"""
1.编号：id，主键，自动递增，大整型
2.短网址信息ID：shorturl_id，非空，大整型
3.访问URL：url，非空，变长字符串类型
4.访问IP：ip，变长字符串类型
5.访问地址：address，变长字符串类型
6.访问方法：method，非空，变长字符串类型
7.创建时间：createdAt，非空，日期时间类型
8.修改时间：updatedAt，非空，日期时间类型
"""


# 统计模型
class PageView(Base):
    __tablename__ = "pageview"
    id = Column(BIGINT, primary_key=True)
    shorturl_id = Column(BIGINT, nullable=False)
    url = Column(VARCHAR(255), nullable=False)
    ip = Column(VARCHAR(100))
    address = Column(VARCHAR(255))
    method = Column(VARCHAR(20), nullable=False)
    createdAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)


if __name__ == "__main__":
    import mysql.connector  # 数据库连接驱动
    from sqlalchemy import create_engine  # 创建连接引擎

    mysql_configs = dict(
        db_host="127.0.0.1",
        db_name="short_url",
        db_port=3306,
        db_user="root",
        db_pwd="root"
    )

    engine = create_engine(
        'mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'.format(
            **mysql_configs
        ),
        encoding="utf-8",
        echo=True
    )

    metadata.create_all(engine)
    print("生成成功！")
