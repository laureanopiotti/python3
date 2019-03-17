from bs4 import BeautifulSoup
from locators.page_locators import PageLocator 
from parsers.element_parser import ElementParser


class Page:
    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')

    @property
    def elements(self):
        locator = PageLocator.PARENT
        tags = self.soup.select(locator)
        return [ElementParser(e,'Book') for e in tags]