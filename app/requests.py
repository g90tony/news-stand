import urllib.request, json
from .models import Article

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']
    
def get_articles(category):
    
    request_url = base_url.format('top-headlines', api_key)
    
    with urllib.request.urlopen(request_url) as url:
        url_response = url.read()
        response_dict = json.loads(url_response)
        
        response_data = None
        
        if response_dict['results']:
            processing_dict = response_data['results']            
            response_data = processed_data(processing_dict)
        
    return response_data
             