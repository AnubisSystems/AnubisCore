from abc import ABC, abstractmethod

class IKeyValueDBPort(ABC):

    @abstractmethod
    def set(self, key, value):
        pass
    @abstractmethod
    def get(self,key):
        pass


class IPubSubDBPort(ABC):
    @abstractmethod
    def publish(self, channel, value):
        pass
    @abstractmethod
    def subscribe(self, channel):
        pass

class IDocumentDBPort(ABC):

    @abstractmethod
    def set(self, document):
        pass

    @abstractmethod
    def get(self,id):
        pass

    @abstractmethod
    def search(self,search_text):
        pass

    pass

class IVectorSearchPort(ABC):
    @abstractmethod
    def create_embedding(self, text: str) -> list[float]:
        pass

    @abstractmethod
    def search_similar(self, vector: list[float], top_k: int = 5) -> list[dict]:
        pass

    @abstractmethod
    def index_document(self, id: str, vector: list[float], metadata: dict) -> bool:
        pass