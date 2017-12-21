__author__ = 'mingfengma'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Lianjia(Base):
    __tablename__ = 'house'

    id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    region = Column(String(length=50))
    building = Column(String(length=50))
    struct = Column(String(length=10))
    housesize = Column(String(length=10))
    floor = Column(String(length=50))
    syear = Column(String(length=50))
    price = Column(String(length=50))
    url_addr = Column(String(length=50))
    houseinfo = Column(String(length=50))
    posinfo = Column(String(length=50))


class User(Base):
    __tablename__ = 'tuser'

    id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
