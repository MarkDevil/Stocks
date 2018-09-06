__author__ = 'mingfengma'

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class IpInfo(Base):
    __tablename__ = 'ip_info'

    ip = Column(String(length=12))
    port = Column(String(length=10))
