from flask import Flask
from infraestructure.web.ports.server_port import Serverport

def set_content_type(content):
       content.headers['Content-Type'] = 'application/json'
       return content

class FlaskServer(Serverport):
    
    def __init__(self) -> None:     
        self.app = Flask(__name__)
        pass
    
    def getInstancia(self):
        return self.app
    
    def iniciarServidor(self):
      self.getInstancia().debug = True
      self.getInstancia().run()
      pass

    def crearEndPoint(self,rule: str, handler, method : str):
      self.app.add_url_rule(rule = rule, view_func = handler,methods=[method])
      self.app.after_request(set_content_type)
      pass
    
    