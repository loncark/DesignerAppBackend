from flask import Flask
from flask_cors import CORS
import os
import importlib       

def createApp():
    app = Flask(__name__)
    CORS(app)

    controllers = loadControllers()

    for controller in controllers:
        app.register_blueprint(controller.blueprint)

    return app

def loadControllers():
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
