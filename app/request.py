# Getting api key
from app import app
import urllib.request
import json
from models.news import Sources, Articles


#Getting api key
api_key = app.config['NEWS_API_KEY']
#getting source base url
base_url_source = app.config['NEWS_API_SOURCE_URL']
#getting articles base url
base_url_articles = app.config['NEWS_API_ARTICLES_URL']


def get_source():  # get all sources from the news api
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = 'https://newsapi.org/v2/sources?apiKey={}'.format(api_key)
    print(get_source_url)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_sources_results(source_results_list)

    return source_results


def process_sources_results(source_list):
    '''
    Function to process source list result and transform them to a list of Objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')

        source_object = Sources(
            id, name, description, url, category, language)
        source_results.append(source_object)

    return source_results


def get_articles(source_id):
    '''
        Function that gets the json response to our url request using the source id
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(
        source_id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)
    return articles_results





def process_articles_results(articles_list):
    '''
    Function to processes articles list result and transform them to a list of Objects
    '''
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            articles_object = Articles(
                author, title, description, url, urlToImage, publishedAt, content)
            articles_results.append(articles_object)

    return articles_results



   