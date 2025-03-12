class Author:

    all =[]
    def __init__(self,name):
        self.name=name
        self._articles=[]
        self._magazines = []
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value) > 0:
            if not hasattr(self, '_name'):
                self._name=value
        else:
            raise ValueError("Insert Author's name.")
        
    def articles(self):
        return self._articles
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def magazines(self):
        return list({article.magazine for article in self._articles})
    
    def topic_areas(self):
        categories = list({magazine.category for magazine in self.magazines()})
        return categories if categories else None
    

    

        
class Magazine:

    all =[]
    def __init__(self,name,category):
        self.name=name
        self.category=category
        self._articles=[]
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str) and 2 <= len(value) <=16:
            self._name =value
        else:
            raise ValueError('Must a string  between 2 and 16 characters')
            
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value
    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))
 
    def authors(self):
        return list({article.author for article in self._articles})
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

    # Only return authors who have contributed more than 2 articles
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None
            
class Article:
    all=[]
    def __init__(self,author,magazine,title):
        if not isinstance(author,Author):
            raise TypeError('Must be an instance of Author')
        if not isinstance(magazine,Magazine):
            raise TypeError('Must be an instance of Magazine')
        
        self.author=author
        self.magazine=magazine

        self.title=title

        author.articles().append(self)
        magazine.articles().append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        if isinstance(value,str) and 5 <= len(value) <= 50 :
            if not hasattr(self ,'_title'):
                self._title = value
        else:
            raise ValueError('Must be a string between 5 to 50 characters')
        
    