
from infraestructure.web.ports.client_port import CardClienteport
from infraestructure.web.ports.server_port import Serverport
from application.controllers.card_controller import CardController

class Application:
    def __init__(self, server: Serverport, client: CardClienteport):
        self.server = server
        CardController(server = self.server, service = client)
        pass
    def start(self):
       self.server.iniciarServidor()