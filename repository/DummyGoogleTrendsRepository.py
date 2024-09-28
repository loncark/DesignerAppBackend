from interface.repositoryInterface.TrendResearchRepository import TrendResearchRepository
import json

class DummyGoogleTrendsRepository(TrendResearchRepository):
    def __init__(self):
        pass
    
    def getTrends(self, date, country_code):
        filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\TrendPage1.json"   
            
        with open(filePath, 'r') as file:
            data = json.load(file)
            
        return data
    
    def getRelatedQueries(self, keyword):
        if(keyword == ''):
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsRelated.json"
        else:
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsRelated2.json"
            
        with open(filePath, 'r') as file:
            data = json.load(file)
        
        return data
    
    def getInterestByRegion(self, keyword):
        if(keyword == ''):
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsInterest.json"
        else:
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsInterest2.json"
            
        with open(filePath, 'r') as file:
            data = json.load(file)
            
        return data
    
    def getInterestOverTime(self, keyword):
        if (keyword == 'christmas'):
            filePath = 'C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\sample JSONs\\ChartData.json'
        else: 
            filePath = 'C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\sample JSONs\\ChartData2.json'
                
        with open(filePath, 'r') as file:
            data = json.load(file)

        return data