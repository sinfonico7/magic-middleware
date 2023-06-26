from application.configurations.application_configuration import Application
from infraestructure.web.adapters.flask.server_host import FlaskServer
from infraestructure.web.adapters.restclient.native_client import NativeClient

        
if __name__ == "__main__":
     app = Application(FlaskServer(), NativeClient())
     app.start()

