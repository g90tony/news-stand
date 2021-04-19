class Source:
    def __init__(self, id, name, description, url, category, language, country, articles):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        self.articles = articles

    def addArticles(sourceArticles):
        Source.allArticles.append = sourceArticles
        
    def getArticles(self):
        return self.articles
    
    
class Article:
    def __init__(self, author, title, description, url, image_url, published_at, content):
        self.author = author 
        self.title = title 
        self.description = description 
        self.url = url 
        self.image_url = image_url 
        self.published_at = published_at 
        self.content = content 