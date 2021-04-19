import urllib.request, json
from .models import Article

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']