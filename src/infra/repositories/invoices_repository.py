from src.infra.repositories.base_repository import BaseRepository
from domain.models.invoices import Invoices

class InvoicesRepository(BaseRepository):
    def __init__(self):
        super().__init__(Invoices)