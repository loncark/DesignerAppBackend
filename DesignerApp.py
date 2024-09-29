from flask import Flask
from flask_cors import CORS
import importlib

class DesignerApp():
    def __init__(self, providerConfig, repositoryConfig):
        self.flaskInstance = Flask(__name__)
        CORS(self.flaskInstance)

        self.flaskInstance.config.from_object(providerConfig)
        self.flaskInstance.config.from_object(repositoryConfig)

        self.loadControllers()

    def run(self):
        self.flaskInstance.run(debug=True)

    def loadControllers(self):
        config = self.flaskInstance.config
        controllers = []

        for key in list(config.keys()):
            if key.endswith('_PROVIDER'):
                keyName = key[:-9]            # TEXT_GENERATION, DATABASE...  
                providerName = config[key]    # Gemini, Firebase...

                controllerClassName = providerName + 'Controller'
                controllerModule = importlib.import_module('controller.' + controllerClassName)

                serviceClassName = providerName + 'Service'
                serviceModule = importlib.import_module('service.' + serviceClassName)

                repositoryClassName = 'Dummy' + providerName + 'Repository' if config['USE_DUMMY_' + keyName + '_REPO'] else 'Real' + providerName + 'Repository'               
                repositoryModule = importlib.import_module('repository.' + repositoryClassName)
                
                controllerClass = getattr(controllerModule, controllerClassName)
                serviceClass = getattr(serviceModule, serviceClassName)
                repositoryClass = getattr(repositoryModule, repositoryClassName)

                controllers.append(controllerClass(serviceClass(repositoryClass())))

        for controller in controllers:
            self.flaskInstance.register_blueprint(controller.blueprint)
