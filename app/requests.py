import urllib.request, json
from .models import Article

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']
    
def article_instanciator(unprocessed_data):
        processed_data = list()
    
    for item in unprocessed_data:
        # id = item.get('id')
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        image_url = item.get('image_url')
        published_at = item.get('published_at')
        content = item.get('content')
        
        if author:
            article_instance = Article(author, title, description, url, image_url, published_at, content)
            processed_data.append(article_instance)
            
    return processed_data

    
def get_articles(category):
    
    request_url = base_url.format('top-headlines', api_key)
    
    with urllib.request.urlopen(request_url) as url:
        url_response = url.read()
        response_dict = json.loads(url_response)
        
        response_data = None
        
        if response_dict['results']:
            processing_dict = response_data['results']            
            response_data = article_instanciator(processing_dict)
        
    return response_data
             