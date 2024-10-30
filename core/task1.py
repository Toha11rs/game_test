from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    first_login = Column(DateTime, default=None)
    daily_login_streak = Column(Integer, default=0)
    score = Column(Integer, default=0)

    boosts = relationship("PlayerBoost", back_populates="player")


class Boost(Base):
    __tablename__ = 'boosts'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    boost_type = Column(String(50))
    duration = Column(Integer)


class PlayerBoost(Base):
    __tablename__ = 'player_boosts'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    boost_id = Column(Integer, ForeignKey('boosts.id'))
    created_at = Column(DateTime, default=datetime.now())

    player = relationship("Player", back_populates="boosts")
    boost = relationship("Boost")
