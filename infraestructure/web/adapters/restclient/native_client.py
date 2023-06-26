import requests
from domain.services.card_service import CardService

from infraestructure.web.ports.client_port import CardClienteport

class NativeClient(CardClienteport):  
    def getAllCards(self):
      response = requests.get("https://api.magicthegathering.io/v1/cards")
      cards = response.json()['cards']
      
      cardService = CardService()
      deck = cardService.filterCardsByLanguage(language = "Spanish", cards = cards)
      print(deck)
      return str(deck)