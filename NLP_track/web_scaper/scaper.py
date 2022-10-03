from unicodedata import category
import requests
import os
import string
import re
from bs4 import BeautifulSoup
from http import HTTPStatus
from pathlib import Path

base_url = 'https://www.nature.com'

def get_articles_from_response(response, req_type, dir):
    
    # check the http to see if it is valid url
    if response.status_code == HTTPStatus.OK:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        # check whether it is an empty article
        if len(articles) > 0:
            for article in articles:
                category = article.find('span', {'class': "c-meta__type"}).text
                
                if category == req_type:
                    title = article.find('a').text.strip()
                    for t in title:
                        if t in string.punctuation:
                            title = title.replace(t, '')
                    title = title.replace(' ', '_')
                    link = article.find('a', href=True)['href']
                    article_url = f'{base_url}{link}'
                    filename = dir / f'{title}.txt'
                    # find article url and get the content
                    response = requests.get(article_url)
                    soup2 = BeautifulSoup(response.content, 'html.parser')
                    content = soup2.find('div', {'class' : 'c-article-body'}).text.strip()
                    content_binary = bytes(content, 'utf-8')
                    # add to file with with translated binary content
                    with open(filename, 'wb') as source:
                        source.write(content_binary)
                        
def browse_pages(pages, category):
    for number in range(1, pages + 1):
        page_dir = Path.cwd() / f'Page_{number}'
        os.mkdir(page_dir)
        page_url = f'{base_url}/nature/articles?sort=PubDate&year=2020'
        url = f'{page_url}&page={number}'
        response = requests.get(url)
        get_articles_from_response(response, category, page_dir)
        
    print('Saved all articles')
    
def main():
    pages = int(input('Enter the page number:\n> '))
    articles_type = input('Enter the category of article:\n> ') # News
    browse_pages(pages, articles_type)
    
if __name__ == '__main__':
    main()   