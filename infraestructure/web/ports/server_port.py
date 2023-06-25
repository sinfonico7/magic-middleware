from abc import ABC, abstractmethod

class Serverport(ABC):

   @abstractmethod
   def getInstancia(self):
      pass

   @abstractmethod
   def iniciarServidor(self):
      pass

   @abstractmethod
   def crearEndPoint(self, rule: str, handler: any,method: str):
      pass