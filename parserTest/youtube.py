import requests
from bs4 import BeautifulSoup as BS


r = requests.get('https://www.youtube.com/')
soup = BS(r.content, 'lxml')

print(soup)


# count = 0
# for i in soup.select('.items > .article-summary'):
#     count += 1
#     title = i.select('.caption > a')
#     print(f'{count}. {title[0].text.strip()}')
