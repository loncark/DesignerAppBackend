from flask import Flask
from flask_cors import CORS
import os
import importlib
from config import ProductionConfig, DevelopmentConfig, TestingConfig    

def createApp(configName=None):
    app = Flask(__name__)
    CORS(app)

    if configName == 'prod':
        app.config.from_object(ProductionConfig)
    elif configName == 'test':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    controllers = loadControllers(app.config)

    for controller in controllers:
        app.register_blueprint(controller.blueprint)

    return app

def loadControllers(config):
    rootDirPath = os.path.dirname(os.path.abspath(__file__))
    controllerDirPath = os.path.join(rootDirPath, 'controller')
    fileNames = os.listdir(controllerDirPath)

    controllers = []
    for fileName in fileNames:
        if fileName.endswith('.py') and not fileName.startswith('__'):
            apiName = fileName[:-13]

            controllerClassName = apiName + 'Controller'
            controllerModule = importlib.import_module('controller.' + controllerClassName)

            serviceClassName = apiName + 'Service'
            serviceModule = importlib.import_module('service.' + serviceClassName)

            if config['USE_DUMMY_' + apiName.upper() + '_REPO']:
                repositoryClassName = 'Dummy' + apiName + 'Repository'
            else:
                repositoryClassName = 'Real' + apiName + 'Repository'
                
            repositoryModule = importlib.import_module('repository.' + repositoryClassName)
            
            controllerClass = getattr(controllerModule, controllerClassName)
            serviceClass = getattr(serviceModule, serviceClassName)
            repositoryClass = getattr(repositoryModule, repositoryClassName)

            controllers.append(controllerClass(serviceClass(repositoryClass())))

    return controllers

if __name__ == '__main__':
    app = createApp()
    app.run(debug=True)
