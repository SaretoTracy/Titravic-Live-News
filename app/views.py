from flask import render_template
from app import app
from .request import get_articles,get_articles_by_category_of_the_source, get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news =get_source('general')
    bbc_news = get_source('bbc-news')
    # get articles from al-jazeera-english
    aljazeera = get_source('al-jazeera-english')
    cnn_home = get_source('cnn')
    bbc_news_home = get_source('bbc-news')
    cbc_news = get_source('cbc-news')
    # sports_news = get_articles_by_category_of_the_source('sports')
    # technology_news = get_articles_by_category_of_the_source('technology')
    # science_news = get_articles_by_category_of_the_source('science')

    
    title = 'Titravic Live New'
    return render_template('index.html', title = title, general = general_news,bcc=bbc_news_home,
                           bbc_news=bbc_news,
                           cnn_home=cnn_home,
                           cbc_news=cbc_news,
                           aljazeera=aljazeera,)
    

# @app.route('/news-source/articles/<source_id>')
# def articles(source_id):
#     '''
#     View articles page => function that returns the articles page from a source id 
#     '''
#     # Getting articles based on the source id
#     articles = get_articles(source_id)
#     title = f'{source_id}'

#     return render_template('articles.html', title=title, articles=articles)

@app.route('/tech')
def technology():
    '''
    View technology page function that returns the technology page and its data
    '''
    technology_news = get_source('technology')
    title = 'Technology - News'
    return render_template('tech.html',title=title,technology=technology_news)

# @app.route('/health')
# def health():
#     '''
#     View health page function that returns the health page and its data
#     '''
#     health = get_articles_by_category_of_the_source('health')
#     title = 'Health - Welcome to The best Hot News in the world'
#     return render_template('health.html',
#                            title=title,
#                            health=health
#                            )
                           
                           
                           


