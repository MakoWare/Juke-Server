from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from app.DataBase.database import Base


class Hub(Base):
    __tablename__ = 'hubs'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))


    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __init__(self, name=None):
        self.name = name

