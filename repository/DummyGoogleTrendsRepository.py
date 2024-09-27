from interface.Repository import Repository
import json

class DummyGoogleTrendsRepository(Repository):
    def __init__(self):
        pass
    
    def fetchTrends(self, date, country_code):
        filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\TrendPage1.json"   
            
        with open(filePath, 'r') as file:
            data = json.load(file)
            
        return data
    
    def fetchRelatedQueries(self, keyword):
        if(keyword == ''):
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsRelated.json"
        else:
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsRelated2.json"
            
        with open(filePath, 'r') as file:
            data = json.load(file)
        
        return data
    
    def fetchInterestByRegion(self, keyword):
        if(keyword == ''):
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsInterest.json"
        else:
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsInterest2.json"
            
        with open(filePath, 'r') as file:
            data = json.load(file)
            
        return data
    
    def fetchInterestOverTime(self, keyword):
        if (keyword == 'christmas'):
            filePath = 'C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\sample JSONs\\ChartData.json'
        else: 
            filePath = 'C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\sample JSONs\\ChartData2.json'
                
        with open(filePath, 'r') as file:
            data = json.load(file)

        return data