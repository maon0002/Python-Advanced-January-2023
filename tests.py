import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_news_articles():
    base_url = 'https://news.bg/bulgaria?page='
    page_number = 1
    articles = []
    key_words = ['домашно насилие', 'насилие върху жени', 'жена', 'убита', 'изнасилване']

    while True:
        url = base_url + str(page_number)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles_div = soup.find_all('div', {'class': 'news-item'})

        if not articles_div:
            break

        for article_div in articles_div:
            article = {}
            article['date'] = article_div.find('div', {'class': 'news-date'}).text.strip()
            article['header'] = article_div.find('a').text.strip()
            article['link'] = article_div.find('a')['href']

            article_response = requests.get(article['link'])
            article_soup = BeautifulSoup(article_response.content, 'html.parser')
            article_text = article_soup.find('div', {'class': 'text-content'}).text.strip().lower()

            article_key_words = []
            for key_word in key_words:
                if key_word in article_text:
                    article_key_words.append(key_word)

            article['key_words'] = ', '.join(article_key_words)
            articles.append(article)

        page_number += 1

    return articles


def main():
    articles = get_news_articles()
    df = pd.DataFrame(articles)
    df = df[df['key_words'] != '']
    print(df)


if __name__ == '__main__':
    main()
