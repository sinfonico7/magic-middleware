import requests
from infraestructure.web.adapters.restclient.mappers.native_client_mapper import NativeMapperClient
from infraestructure.web.ports.client_port import CardClienteport


class NativeClient(CardClienteport):  
    def getAllCards(self):
      response = requests.get("https://api.magicthegathering.io/v1/cards")
      cards = response.json()['cards']
      mapper =  NativeMapperClient()    
      deck = mapper.getForeignNamesFromCards(cards)
      return str(deck)