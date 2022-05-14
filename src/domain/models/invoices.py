from email.policy import default
from src.config import Base

from sqlalchemy import Column, Integer, Float, Boolean
from sqlalchemy.orm import relationship


class Invoices(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    sotre_id = Column(Integer, nullable=False)
    opened = Column(Boolean, default=True)
    table = Column(Integer)
    price = Column(Float, nullable=False)
    invoices_items = relationship('InvoicesItems')

    def __repr__(self): # pragma: no cover
        return f'Invoice {self.id}'