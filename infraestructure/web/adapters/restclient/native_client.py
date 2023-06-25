import requests

from infraestructure.web.ports.client_port import CardClienteport

class NativeClient(CardClienteport):
    def getAllCards(self):
      response = requests.get("https://api.magicthegathering.io/v1/cards")
      data = response.json()
      # incluir mapper
      return data