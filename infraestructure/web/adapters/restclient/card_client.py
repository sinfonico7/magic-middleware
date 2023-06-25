import json
from mtgsdk import Card

from infraestructure.web.ports.client_port import CardClienteport


class MagicCardClient(CardClienteport):


    def getAllCards(self):
        card = Card.all()
        
        json_objeto = json.dumps(card.__dict__)
        return json_objeto
        