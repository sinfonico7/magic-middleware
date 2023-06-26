import json
from mtgsdk import Card

from infraestructure.web.ports.client_port import CardClienteport


class MagicCardClient(CardClienteport):


    def getAllCards(self):
        cards = Card.all()
        json_objeto = json.dumps(cards.__dict__)
        return json_objeto
        