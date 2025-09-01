# SERVICES
from anubis_core.features.product.ports import IProductAdapter
from anubis_core.features.product.models import CoreProduct
from anubis_openai_adapters.openai import OpenAIAdapter


class ProductsService():

    def __init__(self, product_adapter : IProductAdapter, open_ia_adapter: OpenAIAdapter ):
        self.product_adapter = product_adapter    
        self.open_ia_adapter = open_ia_adapter    

    def save_product(self, product: CoreProduct) -> CoreProduct:
        if product.id:
            return self.product_adapter.send_product(product)
        else :
            return self.product_adapter.create_product(product)
        

    def get_product(self, id_product:int)-> CoreProduct:
        return self.product_adapter.get_product(id_product)
    
    def search_id(self, page, rows,  *args, **kwargs) -> list[str]:        
        return self.product_adapter.search_id(page,rows,*args, **kwargs)        
            