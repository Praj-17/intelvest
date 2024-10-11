# app/models.py

from datetime import datetime, date
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PortfolioModel(Base):
    __tablename__ = 'portfolio'

    p_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    portfolio_name = Column(String(255), nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    created_at = Column(Date, default=date.today)

    def to_dict(self):
        return {
            "p_id": self.p_id,
            "user_id": self.user_id,
            "portfolio_name": self.portfolio_name,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
