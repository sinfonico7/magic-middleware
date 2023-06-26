from application.configurations.application_configuration import Application
from infraestructure.web.adapters.flask.server_host import FlaskServer
from infraestructure.web.adapters.restclient.native_client import NativeClient

#flask_server = 
#fordebugInstance = flask_server.getInstancia()
        
if __name__ == "__main__":
     app = Application(FlaskServer(), NativeClient())
     app.start()
