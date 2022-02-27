from flask import render_template
from app import app
from .request import get_articles_from_source_selected, get_source,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news =get_source('general')
    bbc_news = get_articles_from_source_selected('bbc-news', '8')
    # get articles from al-jazeera-english
    aljazeera = get_articles_from_source_selected('al-jazeera-english', '8')
    cnn_home = get_articles_from_source_selected('cnn', '1')
    bbc_news_home = get_articles_from_source_selected('bbc-news', '2')
    cbc_news = get_articles_from_source_selected('cbc-news', '2')

    
    title = 'Home - TITRAVIC LIVE NEWS '
    return render_template('index.html',
                           title=title,
                           bcc=bbc_news_home,
                           bbc=bbc_news,
                           cnn_home=cnn_home,
                           general=general_news,
                           cbc_news=cbc_news,
                           aljazeera=aljazeera,
                           )
    

@app.route('/articles/<source_id>')
def articles(source_id):
    '''
    View articles page => function that returns the articles page from a source id 
    '''
    # Getting articles based on the source id
    articles_news = get_articles("general")
    title = f'{source_id}'

    return render_template('articles.html', title=title, articles=articles_news)


 
                           
                           


