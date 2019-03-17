from locators.element_locators import ElementLocator 

class ElementParser:
    '''Find out the data about a given element'''
    def __init__(self,parent,element_type):
        self.parent = parent
        self.type = element_type

    def __repr__(self):
        return f'<Element {self.type}: {self.name}.>'
    
    @property
    def rating(self):
        locator = ElementLocator.RATING 
        return [c for c in self.parent.select_one(locator)['class'] if c != 'star-rating']
    
    @property
    def name(self):
        locator = ElementLocator.NAME
        return self.parent.select_one(locator)['title']
    
    @property
    def price(self):
        locator = ElementLocator.PRICE
        return self.parent.select_one(locator).string

    @property
    def instock(self):
        locator = ElementLocator.IN_STOCK
        return [e.upper() for e in self.parent.select_one(locator).contents]
    


