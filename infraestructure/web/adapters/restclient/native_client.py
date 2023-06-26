import requests
from domain.services.card_service import CardFilter
from infraestructure.web.adapters.restclient.mappers.native_client_mapper import NativeMapperClient
from infraestructure.web.ports.client_port import CardClienteport


class NativeClient(CardClienteport):  
    def getAllCards(self):
      mapper =  NativeMapperClient()
      filter =  CardFilter()
      response = requests.get("https://api.magicthegathering.io/v1/cards")
      cards = response.json()['cards']    
      deck = mapper.getForeignNamesFromCards(cards)
      deck = filter.filterByLanguaje(languaje="Spanish", deck=deck)
      return str(deck)