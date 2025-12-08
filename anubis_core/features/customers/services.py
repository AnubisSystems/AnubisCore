# SERVICES
from anubis_core.features.customers.ports import ICustomerAdapter
from anubis_core.features.customers.models import CoreCustomer
from anubis_openai_adapters.openai import OpenAIAdapter
from .exceptions import CustomerAplicacionExceptions, CustomerApplicactionException


class ProductsService():

    def __init__(self, customer_adapter : ICustomerAdapter, open_ia_adapter: OpenAIAdapter ):
        self.customer_adapter = customer_adapter    
        self.open_ia_adapter = open_ia_adapter    

    def save_product(self, customer: CoreCustomer) -> CoreCustomer:
        if customer.id:
            return self.customer_adapter.send_customer(customer)
        else :
            return self.customer_adapter.create_customer(customer)
        

    def get_product(self, id_customer:int)-> CoreCustomer:
        _product = self.customer_adapter.get_customer_id(id_customer)
        if _product == None: 
            raise CustomerApplicactionException(
                CustomerAplicacionExceptions.CUSTOMER_NOT_FOUND, 
                {"customer" : id_customer})
        return _product