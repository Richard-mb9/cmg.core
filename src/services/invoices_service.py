from typing import List
from src.utils.handlers import object_as_dict
from domain.models.invoices import Invoices
from domain.models.invoices_items import InvoicesItems
from infra.repositories.invoices_repository import InvoicesRepository
from infra.repositories.invoices_items_repository import InvoicesItemsRepository
from services.products_service import ProductsService
from utils.errors import UnprocessableEntityError

class InvoiceService:
    def __init__(self):
        self.repository = InvoicesRepository()
        self.invoice_items_repository = InvoicesItemsRepository()

    def create(self, data):
        invoice = Invoices(
            store_id=data.get('store_id'),
            table=data.get('table'),
            price=0.0
        )
        result = self.repository.create(invoice)
        return {'id': result.id}
    
    def update(self, id, data_to_update):
        self.repository.update(id, data_to_update)
    
    def read_by_id(self, id) -> dict:
        result =  self.repository.read_by_id(id)
        return object_as_dict(result)
    
    def list(self) -> list:
        return object_as_dict(self.repository.list())
    
    def delete(self, id):
        self.repository.delete(id)

    def __read_invoice_by_id(self, invoice_id) -> Invoices:
        return self.repository.read_by_id(invoice_id)
    
    def __get_products_prices(self, items: list):
        """
        recebe uma lista de produtos, e busca no banco de dados todos os dados destes produtos,
        depois cria uma um dicionario que como chaves tem os ids de cada produto, e como valor
        os preços unitarios destes produtos
        """
        products_ids = set()
        for item in items:
            products_ids.add(item.get('id'))
        products = ProductsService().batch_get_by_id(list(products_ids))
        products_prices = {}
        for product in products:
            products_prices[product.id] = product.price
        return products_prices
            
    def add_items(self, invoice_id, items: list):
        invoice = self.__read_invoice_by_id(invoice_id)
        if invoice.opened == False:
            UnprocessableEntityError("the invoice sent has already been closed")

        items_for_create = []
        products_prices = self.__get_products_prices(items)
        for item in items:
            product_price = products_prices.get(item.get('product_id'))
            items_for_create.append(
                InvoicesItems(
                    invoice_id=invoice_id,
                    product_id=item.get('product_id'),
                    quantity=item.get('quantity'),
                    unity_price=product_price,
                    price=(product_price * item.get('quantity'))
                )
            )
        self.invoice_items_repository.batch_create(items_for_create)
        