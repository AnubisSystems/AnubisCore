
from abc import ABC, abstractmethod


class ICloudDocumentsAdapter(ABC):
    
    @abstractmethod
    def push(self,  folder, filename, content):
        pass

    @abstractmethod
    def pull(self,  folder, filename):
        pass

    @abstractmethod
    def list(self, folder):
        pass

