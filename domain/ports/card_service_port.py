
from abc import ABC, abstractmethod

from domain.model.deck import Deck


class CardServiceAbstract(ABC):
    
    @abstractmethod
    def filterCardsByLanguage(self,language:str, cards: list) -> Deck:
        pass