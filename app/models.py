from sqlalchemy import Boolean, Column, Integer, Float, BigInteger

from .database import Base

import time

class TrafficlightPhase(Base):
    __tablename__ = "trafficlight_phases"
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    is_green = Column(Boolean)
    phase_length = Column(Float)
    commit_time = Column(Float, default=time.time())