from flask import Flask
from flask_cors import CORS
import os
import importlib
from config import ProductionConfig, DevelopmentConfig, TestingConfig   
from repository.DummyFirebaseRepository import DummyFirebaseRepository
from repository.RealFirebaseRepository import RealFirebaseRepository    

def createApp(configName):
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
            controllerClassName = fileName[:-3]
            module = importlib.import_module('controller.' + controllerClassName)

            controllerClass = getattr(module, controllerClassName)
            controllers.append(controllerClass())

    return controllers


if __name__ == '__main__':
    app = createApp()
    app.run(debug=True)
