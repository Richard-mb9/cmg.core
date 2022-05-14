from src.infra.repositories.base_repository import BaseRepository


class InvoicesItemsRepository(BaseRepository):
    def __init__(self, entity):
        super().__init__(entity)