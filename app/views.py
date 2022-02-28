from flask import render_template
from app import app
from .request import get_source,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news =get_source('general')
    

    articles_news = get_articles("general")

    
    title = 'Home - TITRAVIC LIVE NEWS '
    return render_template('index.html',
                           title=title,
                           general=general_news,
                           articles=articles_news
                           )



@app.route('/articles')
def articles():
    '''
    View articles page => function that returns the articles page from a source id 
    '''
    # Getting articles based on the source id
    articles = get_articles("general")
    title = "TITRAVIC"

    return render_template('articles.html', title=title, articles=articles)

    



 
                           
                           


