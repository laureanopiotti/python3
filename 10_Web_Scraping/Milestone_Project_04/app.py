import requests
from page.page import Page

page_content = requests.get('http://books.toscrape.com').content
page = Page(page_content)

for e in page.elements:
    print(e.instock)