class Source:
    def __init__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


    def addArticles(sourceArticles):
        Source.allArticles.append = sourceArticles
        
    def getArticles(self):
        return self.articles
    
    
class Article:
    def __init__(self, author, title, description, url, image_url, published_at, source, content):
        self.author = author 
        self.title = title 
        self.description = description 
        self.url = url 
        self.image_url = image_url 
        self.published_at = published_at 
        self.source = source 
        self.content = content 