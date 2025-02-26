class Author:
    def __init__(self,name):
        self.name=name
        self._articles=[]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value) >0:
            if not hasattr(self, '_name'):
                self._name=value
        else:
            raise ValueError("Insert Author's name.")
        
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list({article.magazine for article in self._articles})
        
class Magazine:
    def __init__(self,name,category):
        self.name=name
        self.category=category
        self._articles=[]

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
    def category(self,value):
        if isinstance(value,str) and len(value) > 0:
            self._category =value
        else:
            raise ValueError('Must a string')
            
    def articles(self):
        return self._articles
        
    def authors(self):
        return list({article.author for article in self._articles})

            
class Article:
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

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        if isinstance(value,str) and 5 <= len(value) >= 50 :
            if not hasattr(self ,'_title'):
                self._title = value
        else:
            raise ValueError('Must be a string between 5 to 50 characters')