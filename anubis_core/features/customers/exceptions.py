from anubis_core.common.exceptions import EnumExceptionsTemplate, AnubisBaseAplicationException

class CustomerAplicacionExceptions(EnumExceptionsTemplate):    
    CUSTOMER_NOT_FOUND = ("customer_not_found", "El producto {customer} no se ha encontrado en el sistema")
    

class CustomerApplicactionException(AnubisBaseAplicationException):
    def __init__(self, codigo_error, contexto=None, original=None):
        super().__init__(CustomerApplicactionException, codigo_error, contexto, original)
