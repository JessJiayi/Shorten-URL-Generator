# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base  # 模型继承的父类
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, CHAR, DATE # mysql字段类型
from sqlalchemy import Column  # 指定字段类

Base = declarative_base()
metadata = Base.metadata

class ShortUrl(Base):
    __tablename__ = "shorturl"
    id = Column(BIGINT, primary_key=True)
    url = Column(VARCHAR(255), unique=True, nullable=False)
    code = Column(CHAR(8), unique=True, nullable=False)
    uuid = Column(CHAR(32), unique=True, nullable=False)
    createdAt = Column(DATE, nullable=False)
    updatedAt = Column(DATE, nullable=False)


class PageView(Base):
    __tablename__ = "pageview"
    id = Column(BIGINT, primary_key=True)
    shorturl_id = Column(BIGINT, nullable=False)
    url = Column(VARCHAR(255), nullable=False)
    ip = Column(VARCHAR(100))
    address = Column(VARCHAR(255))
    method = Column(VARCHAR(20), nullable=False)
    createdAt = Column(DATE, nullable=False)
    updatedAt = Column(DATE, nullable=False)


if __name__ == "__main__":  
    from sqlalchemy import create_engine  

    mysql_configs = dict(
        db_host="ec2-54-172-175-251.compute-1.amazonaws.com",
        db_name="d8nt0t0evtddcp",
        db_port=5432,
        db_user="ocklswkhlicvau",
        db_pwd="0ef0864eb874ca4af692ff36d91ed54c5ca6bf25f7d5e10f84e3cda62b59a3c8"
    )

    engine = create_engine(
        'postgresql+psycopg2://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'.format(
            **mysql_configs
        ),
        encoding="utf-8",
        echo=True
    )

    metadata.create_all(engine)
    print("successful")
