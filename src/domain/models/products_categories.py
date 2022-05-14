from src.config import Base

from sqlalchemy import Column, Integer, String


class ProductsCategories(Base):
    __tablename__ = 'products_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self): # pragma: no cover
        return f'Category {self.name}'