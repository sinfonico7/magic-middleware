from infraestructure.web.ports.client_port import CardClienteport
from infraestructure.web.ports.server_port import Serverport


class CardController:

    def __init__(self,server : Serverport, service : CardClienteport) -> None:
        server.crearEndPoint(rule = '/cards',handler = service.getAllCards,method = 'GET')
        pass


