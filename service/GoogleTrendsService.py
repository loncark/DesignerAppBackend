import serpapi, json
from config import SERPAPI_API_KEY
from datetime import datetime, timedelta
from flask import jsonify

# change frequency to realtime for realtime searches,
# delete the date field and add "cat": "all",

# LEAVE global_test=True TO NOT DRAIN THE API LIMIT (45/mo for etsy, a lot for trademark, 100/mo for Trends, interest and related together)

global_test=True

def fetchTrends(date, country_code, test=global_test):
    if test:
        filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\TrendPage1.json"   
        
        with open(filePath, 'r') as file:
            data = json.load(file)
        
        return data
    
    else: 
        params = {
            "engine": "google_trends_trending_now",
            "frequency": "daily",
            "geo": country_code,
            "date": date,
            "api_key": SERPAPI_API_KEY
        }
        
        try:
            search = serpapi.search(params)
            results = search.as_dict()
            return results
        except Exception as e:
            if e.status_code == 429:
                return json.dumps({"message": "API limit of 100 searches per month exceeded."}), 429
            else:
                print(e)

def fetchRelatedQueries(keyword, test=global_test):
    if test:
        if(keyword == ''):
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsRelated.json"
        else:
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsRelated2.json"
        
        with open(filePath, 'r') as file:
            data = json.load(file)
    
        return data

    else:
        params = {
            "engine": "google_trends",
            "q": keyword,
            "data_type": "RELATED_QUERIES",
            "api_key": SERPAPI_API_KEY
        }
        
        try:
            search = serpapi.search(params)
            results = search.as_dict()
            return results
        except Exception as e:
            if e.status_code == 429:
                return json.dumps({"message": "API limit of 100 searches per month exceeded."}), 429
            else:
                print(e)

def fetchInterestByRegion(keyword, test=global_test):
    if test:
        if(keyword == ''):
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsInterest.json"
        else:
            filePath = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsInterest2.json"
        
        with open(filePath, 'r') as file:
            data = json.load(file)
        
        return data

    else:
        params = {
            "engine": "google_trends",
            "q": keyword,
            "data_type": "GEO_MAP_0",
            "api_key": SERPAPI_API_KEY
        }
        
        try:
            search = serpapi.search(params)
            results = search.as_dict()
            return results
        except Exception as e:
            if e.status_code == 429:
                return json.dumps({"message": "API limit of 100 searches per month exceeded."}), 429
            else:
                print(e)

def fetchInterestOverTime(keyword, test=global_test):
    try:
        if test:
            if (keyword == 'christmas'):
                filePath = 'C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\sample JSONs\\ChartData.json'
            else: 
                filePath = 'C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\sample JSONs\\ChartData2.json'
            
            with open(filePath, 'r') as file:
                data = json.load(file)

        else:
            if not keyword:
                return jsonify({'error': 'Keyword is required'}), 400
            
            endDate = datetime.now().strftime('%Y-%m-%d')
            startDate = (datetime.now() - timedelta(days=5*365)).strftime('%Y-%m-%d')

            params = {
                "engine": "google_trends",
                "q": keyword,
                "data_type": "TIMESERIES",
                "api_key": SERPAPI_API_KEY,
                "date": f"{startDate} {endDate}"
            }

            search = serpapi.search(params)
            data = search.as_dict()

        processed_data = extractDatesAndValues(data)

        return jsonify({'data': processed_data})

    except Exception as e:
        print("Error processing trend data: ", e)
        return jsonify({'error': "Error processing trend data."})
    
def extractDatesAndValues(data):
    timeline_data = data['interest_over_time']['timeline_data']
        
    processed_data = []
    for item in timeline_data:
        date = datetime.fromtimestamp(int(item['timestamp']))
        value = item['values'][0]['extracted_value']
        processed_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'value': value
        })

    return processed_data
