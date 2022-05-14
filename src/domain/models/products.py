from src.config import Base

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


products_categories_products = Table('products_categories_products', Base.metadata,
    Column('product_id', Integer,ForeignKey('products.id')),
    Column('category_id', Integer,ForeignKey('products_categories.id'))
)


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, nullable=False)
    image_url = Column(String)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    categories = relationship('ProductsCategories', secondary=products_categories_products)

    def __repr__(self): # pragma: no cover
        return f'Product {self.name}'