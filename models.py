from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.db_session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)

    notes = relationship('Note', back_populates='user')

class Note(Base):
    __tablename__='notes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_id'))
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)

    user = relationship('User', back_populates='notes')
