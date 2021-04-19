import urllib.request, json
from .models import Article, Source

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']
    
def source_instanciator(unprocessed_data):
    processed_data = list()
    
    for item in unprocessed_data:
        id = item.get("id")
        name = item.get("name")
        description = item.get("description")
        url = item.get("url")
        category = item.get("category")
        language = item.get("language")
        country = item.get("country")

        
        if name:
            source_instance = Source(id, name, description, url, category, language, country)
            processed_data.append(source_instance)
            
    return processed_data


def article_instanciator(unprocessed_data):
    processed_data = list()
    
    for item in unprocessed_data:
        # id = item.get('id')
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        image_url = item.get('urlToImage')
        published_at = item.get('published_at')
        content = item.get('content') or item.get('description')
        
        
        source = item.get('source')
        source_name = source['name']
        
        if author:
            article_instance = Article(author, title, description, url, image_url, published_at, source_name, content)
            processed_data.append(article_instance)
            
    return processed_data

    
def get_articles(category):
    
    request_url = base_url.format(category, api_key)
    
    with urllib.request.urlopen(request_url) as url:
        url_response = url.read()
        response_dict = json.loads(url_response)
        
        response_data = None
        
        if response_dict['articles']:
            processing_dict = response_dict['articles']            
            response_data = article_instanciator(processing_dict)
        
    return response_data

def get_sources():
    request_url = base_url.format('sources?', api_key)
    
    with urllib.request.urlopen(request_url) as url:
        url_response = url.read()
        response_dict = json.loads(url_response)
        
        response_data = list()
        
        if response_dict['sources']:
            processing_dict = response_dict['sources']     
            response_data = source_instanciator(processing_dict)
            print(response_data)
            
            
    return response_data
            