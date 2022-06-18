from sqlalchemy import Boolean, Column, Integer, String, Float

from database import Base


class Duma(Base):
    __tablename__ = "duma"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    text = Column(String)
    text_length = Column(Integer)
    text_w_length = Column(Integer)
    positive_prob = Column(Float)
    negative_prob = Column(Float)
    positive = Column(String)
    performances = Column(Integer)
    year = Column(Integer)