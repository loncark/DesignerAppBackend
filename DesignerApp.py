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
                controllerClass = self.loadClass('Controller', controllerClassName, keyName)
                
                serviceClassName = providerName + 'Service'
                serviceClass = self.loadClass('Service', serviceClassName, keyName)

                repositoryClassName = 'Dummy' + providerName + 'Repository' if config['USE_DUMMY_' + keyName + '_REPO'] else 'Real' + providerName + 'Repository'               
                repositoryClass = self.loadClass('Repository', repositoryClassName, keyName)

                controllers.append(controllerClass(serviceClass(repositoryClass())))

        for controller in controllers:
            self.flaskInstance.register_blueprint(controller.blueprint)

    def loadClass(self, classType, className, keyName):
        try:
            interfaceName = keyName.lower().replace('_', ' ').title().replace(' ', '') + classType  # TEXT_GENERATION -> TextGenerationController
            interfaceModule = importlib.import_module('interface.' + classType.lower()  + 'Interface.' + interfaceName)
            interface = getattr(interfaceModule, interfaceName)

            classModule = importlib.import_module(classType.lower() + '.' + className)
            cls = getattr(classModule, className)

        except ImportError as e:
            raise ImportError(f'Failed to import {className} or its interface {str(e)}')
        except AttributeError as e:
            raise AttributeError(f'Class/Interface not found: {str(e)}')

        if not issubclass(cls, interface):
            raise TypeError(f"{cls.__name__} does not implement {interface.__name__}")
        
        return cls
