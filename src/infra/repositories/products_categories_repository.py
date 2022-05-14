from src.infra.repositories.base_repository import BaseRepository
from domain.models.products_categories import ProductsCategories

class ProductsCategoriesRepository(BaseRepository):
    def __init__(self):
        super().__init__(ProductsCategories)