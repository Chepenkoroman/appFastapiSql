from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class Duma(Base):
    __tablename__ = "duma"

    id = Column(Integer, primary_key=True, index=True)
    speach = Column(String)