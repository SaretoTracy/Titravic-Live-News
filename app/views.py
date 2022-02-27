from flask import render_template
from app import app
from .request import get_articles,get_articles_by_category_of_the_source, get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    business_news =get_source('general')
    # sports_news = get_articles_by_category_of_the_source('sports')
    # technology_news = get_articles_by_category_of_the_source('technology')
    # science_news = get_articles_by_category_of_the_source('science')

    
    title = 'Titravic Live New'
    return render_template('index.html', title = title, business = business_news)
    

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
                           
                           
                           


