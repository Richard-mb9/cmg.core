from typing import List
from src.domain.models.products import Products
from src.infra.repositories.base_repository import BaseRepository
from src.config import get_session


class ProductsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Products)

    def list_by_store_id(self, store_id) -> List[Products]:
        session = get_session()
        return session.query(self.entity).filter_by(store_id=store_id).all()