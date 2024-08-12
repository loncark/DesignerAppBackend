import serpapi, json, os
from config import SERPAPI_API_KEY
from datetime import datetime, timedelta
import requests, json
from flask import jsonify, request

# change frequency to realtime for realtime searches,
# delete the date field and add "cat": "all",

def fetchTrends(date, country_code):
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
    except serpapi.SerpApiClientException as e:
        if e.status_code == 429:
            error_response = {
                "message": "API limit of 100 searches per month exceeded."
            }
            return json.dumps(error_response), 429
        else:
            raise

def fetchRelatedQueries(keyword):
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
    except serpapi.SerpApiClientException as e:
        if e.status_code == 429:
            error_response = {
                "message": "API limit of 100 searches per month exceeded."
            }
            return json.dumps(error_response), 429
        else:
            raise

def fetchInterestByRegion(keyword):
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
    except serpapi.SerpApiClientException as e:
        if e.status_code == 429:
            error_response = {
                "message": "API limit of 100 searches per month exceeded."
            }
            return json.dumps(error_response), 429
        else:
            raise

def fetchInterestOverTime(keyword):
    if not keyword:
        return jsonify({'error': 'Keyword is required'}), 400

    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=5*365)).strftime('%Y-%m-%d')

    url = f"https://serpapi.com/search.json?engine=google_trends&q={keyword}&date={start_date} {end_date}&api_key={SERPAPI_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract and process the timeline data
        timeline_data = data['interest_over_time']['timeline_data']
        
        processed_data = []
        for item in timeline_data:
            date = datetime.fromtimestamp(int(item['timestamp']))
            value = item['values'][0]['extracted_value']
            processed_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'value': value
            })

        return jsonify({'data': processed_data})

    except Exception as e:
        print(f"Error processing data: {str(e)}")
        return jsonify({'error': 'Failed to process trend data'}), 500


# TEST FUNCTIONS TO NOT DRAIN THE API LIMIT (45/mo for etsy, a lot for trademark, 100/mo for Trends, interest and related together)
def fetchTrends2(keyword, page):
    file_path = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\TrendPage1.json"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def fetchRelatedQueries2(keyword):
    if(keyword == ''):
        file_path = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsRelated.json"
    else:
        file_path = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsRelated2.json"

    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def fetchInterestByRegion2(keyword):
    if(keyword == ''):
        file_path = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsInterest.json"
    else:
        file_path = r"C:\Users\Kristina\Documents\Diplomski rad\DesignerAppBackend\sample JSONs\KeywordsInterest2.json"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def fetchInterestOverTime2(keyword):
    try:
        if (keyword == ''):
            with open('C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\sample JSONs\\ChartData.json', 'r') as file:
                data = json.load(file)
        else:
            with open('C:\\Users\\Kristina\\Documents\\Diplomski rad\\DesignerAppBackend\\sample JSONs\\ChartData2.json', 'r') as file:
                data = json.load(file)

        timeline_data = data['interest_over_time']['timeline_data']
        
        processed_data = []
        for item in timeline_data:
            date = datetime.fromtimestamp(int(item['timestamp']))
            value = item['values'][0]['extracted_value']
            processed_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'value': value
            })

        return jsonify({'data': processed_data})

    except Exception as e:
        print(f"Error processing data: {str(e)}")
        return jsonify({'error': 'Failed to process trend data'}), 500