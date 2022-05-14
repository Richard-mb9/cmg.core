from src.utils.handlers import object_as_dict
from src.infra.repositories.products_categories_repository import ProductsCategoriesRepository
from src.domain.models.products_categories import ProductsCategories


class ProductsCategoriesService:
    def __init__(self):
        self.repository = ProductsCategoriesRepository()

    def create(self, data):
        category = ProductsCategories(
            name=data.get('name')
        )
        result = self.repository.create(category)
        return {'id': result.id}
    
    def read_by_id(self, id) -> dict:
        result =  self.repository.read_by_id(id)
        return object_as_dict(result)

    def update(self, id, data_to_update):
        self.repository.update(id, data_to_update)

    def list(self) -> list:
        return object_as_dict(self.repository.list())

    def delete(self, id):
        self.repository.delete(id)