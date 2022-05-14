from typing import List
from src.security.security import get_user_id_in_token
from src.utils.handlers import object_as_dict
from src.infra.repositories.products_repository import ProductsRepository
from src.domain.models.products import Products


class ProductsService:
    def __init__(self):
        self.repository = ProductsRepository()

    def create(self, data, store_id = None):
        store_id = store_id if store_id is not None else get_user_id_in_token()
        product = Products(
            store_id=store_id,
            image_url=data.get('image_url'),
            name=data.get('name'),
            price=data.get('price')
        )
        result =  self.repository.create(product)
        return {'id': result.id}
    
    def read_by_id(self, id):
        result =  self.repository.read_by_id(id)
        return object_as_dict(result)
    
    def list_by_store_id(self, store_id):
        return object_as_dict(self.repository.list_by_store_id(store_id))

    def update(self, product_id, data_to_update):
        self.repository.update(product_id, data_to_update)
    
    def delete(self, id):
        self.repository.delete(id)
    
    def batch_get_by_id(self, ids: List[int]) -> List[Products]:
        return self.repository.read_by_id_in(ids)
