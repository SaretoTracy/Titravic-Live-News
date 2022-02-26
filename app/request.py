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



   