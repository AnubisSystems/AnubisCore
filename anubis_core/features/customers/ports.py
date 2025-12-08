from abc import ABC, abstractmethod
from anubis_core.features.customers.models import CoreCustomer, CoreCustomerAddress, CoreCustomerHistoryInvoice, CoreCustomersLoyalty, CustomerAdressTypes

"""INTERFACES DE PRODUCTOS A IMPLEMENTAR POR LOS ADAPTADORES ESPECIFICOS
"""

class ICustomerAdapter(ABC):
    """Interface de producto abstracto    
    """
    @abstractmethod
    def get_customer_id(self, id_customer:int)-> CoreCustomer:        
        pass

    @abstractmethod
    def get_customer_email(self, email:str)-> CoreCustomer:        
        pass

    @abstractmethod
    def create_customer(self, customer: CoreCustomer)-> CoreCustomer:        
        pass

    @abstractmethod
    def send_customer(self, customer: CoreCustomer)-> CoreCustomer:        
        pass    

    