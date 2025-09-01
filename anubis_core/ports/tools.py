from abc import ABC, abstractmethod

class ITemplateEnviromentPort(ABC):

    @abstractmethod
    def render(self,template,*args, **kwargs) -> str:
        pass
