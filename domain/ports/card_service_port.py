
from abc import ABC, abstractmethod


class CardServiceAbstract(ABC):
    
    @abstractmethod
    def filterCardsByLanguage(self,language:str, cards:list):
        pass