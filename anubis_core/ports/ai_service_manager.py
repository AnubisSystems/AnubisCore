# INTEFACES

from abc import ABC, abstractmethod
from anubis_core.models.ai_manager import AIRecipe, AIRecipeList


class IAIServicesManagerPort(ABC):

    @abstractmethod
    def get_chat_completion(self, model, prompt,image_base64 = None, context=None) -> tuple[str, AIRecipe]:
        pass

    @abstractmethod
    def get_chat_completion_json(self, model, prompt,image_base64 = None, context=None) -> tuple[dict, AIRecipe]:
        pass
    

class IAIServicesPort(ABC):
    @property
    @abstractmethod    
    def name(self) -> str:
        pass

    @abstractmethod
    def process(self,*args, **kwargs) -> tuple[dict, AIRecipe]:
        pass

class IAIAnalizeServicePort(ABC):
    
    # @property
    # @abstractmethod
    # def ai_services(self) -> list[IAIServicesPort]:
    #     pass

    
    # @ai_services.setter
    # @abstractmethod   
    # def ai_services(self, value: str) :
    #     pass

    @abstractmethod
    def process(self,ai_services : list[IAIServicesPort], images_base64 : list[str]) -> dict :
        pass
    
    @abstractmethod
    def process_to_text_json(self, image_base64: str) -> tuple[any,AIRecipeList]:
        pass

    @abstractmethod
    def process_to_text(self, image_base64: str) -> tuple[any,AIRecipeList]:
        pass
