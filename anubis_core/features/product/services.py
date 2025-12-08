# SERVICES
from anubis_core.features.product.ports import IProductAdapter, ICategoryAdapter
from anubis_core.features.product.models import CoreProduct, CoreCategory, CoreCategoryProduct
from anubis_openai_adapters.openai import OpenAIAdapter
from .exceptions import ProductApplicactionException, ProductsAplicacionExceptions


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
        _product = self.product_adapter.get_product(id_product)
        if _product == None: 
            raise ProductApplicactionException(
                ProductsAplicacionExceptions.PRODUCT_NOT_FOUND, 
                {"product" : id_product})
        return _product
    
    
    def search_id(self, page, rows,  *args, **kwargs) -> list[str]:        
        return self.product_adapter.search_id(page,rows,*args, **kwargs)        
            
class CategorysService():
    def __init__(self, 
                 category_adapter :ICategoryAdapter, 
                 product_adapter: IProductAdapter):
        self.category_adapter = category_adapter
        self.product_adapter = product_adapter
        
    def save_category(self, category: CoreCategory) -> CoreCategory:
        if category.id:
            return self.category_adapter.send_category(category)
        else:
            return self.category_adapter.create_category(category)    

    def asign_category_product(self, category: CoreCategoryProduct ) -> CoreCategoryProduct:
        pass

    def get_category(self, category_id = None, depth = 0) -> CoreCategory:
        return self.category_adapter.get_category(category_id,depth)

 