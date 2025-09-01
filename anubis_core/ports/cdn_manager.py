# INTEFACES

from abc import ABC, abstractmethod


class ICdnManagerPort(ABC):
    
    @abstractmethod
    def check_filename(self,  filename):
        pass

    @abstractmethod
    def send_file(self, filename, base64,msg):
        pass
    @abstractmethod
    def convert_filename(self, name):
        pass