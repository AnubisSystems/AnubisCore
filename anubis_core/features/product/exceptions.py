from anubis_core.common.exceptions import EnumExceptionsTemplate, AnubisBaseAplicationException

class ProductsAplicacionExceptions(EnumExceptionsTemplate):    
    PRODUCT_NOT_FOUND = ("product_not_found", "El producto {product} no se ha encontrado en el sistema")
    

class ProductApplicactionException(AnubisBaseAplicationException):
    def __init__(self, codigo_error, contexto=None, original=None):
        super().__init__(ProductApplicactionException, codigo_error, contexto, original)
