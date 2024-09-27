from interface.Repository import Repository
import json

class DummyEtsyRepository(Repository):
    def fetchProducts(self, keyword, page):
        if keyword == '':
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\EtsyPage1.json"
        elif keyword == 'cat shirt':
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\EtsyPage2.json"
        elif keyword == 'christmas':
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\EtsyPage3.json"
            
        with open(filePath, 'r') as file:
            data = json.load(file)
            
        return data