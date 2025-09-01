from abc import ABC, abstractmethod

class IWebSearchPort(ABC):

    @abstractmethod
    def search(self,text, rows = 10, page = 1, idSearch=None, image=False) -> list[str]:
        pass
    