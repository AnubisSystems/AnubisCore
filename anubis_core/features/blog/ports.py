from abc import ABC, abstractmethod
from anubis_core.features.blog.models import CorePost

"""INTERFACES DE BLOGS A IMPLEMENTAR POR LOS ADAPTADORES ESPECIFICOS
"""

class IPostAdapter(ABC):
    """Interface de post abstracto    
    """
    @abstractmethod
    def pull_post(self, id_product:int)-> CorePost:
        """busca Retorna un objeto Post con el id proporcionado

        Args:
            id_product (int):

        Returns:
            CoreProduct: 
        """
        pass

    @abstractmethod
    def push_post(self, product:CorePost)-> CorePost:
        pass

    @abstractmethod
    def search_posts(self, search_text:str)-> list[CorePost]:
        pass


