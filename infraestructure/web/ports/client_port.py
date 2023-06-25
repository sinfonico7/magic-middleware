from abc import ABC, abstractmethod

class CardClienteport(ABC):

   @abstractmethod
   def getAllCards(self):
      pass