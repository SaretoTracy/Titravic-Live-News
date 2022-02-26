from flask import render_template
from app import app
from .request import process_sources_results,process_articles_results,get_source,get_articles,get_articles_by_category_of_the_source,get_articles_from_source_selected

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/news-source/articles/<source_id>')
def articles(source_id):
    '''
    View articles page => function that returns the articles page from a source id 
    '''
    # Getting articles based on the source id
    articles = get_articles(source_id)
    title = f'{source_id}'

    return render_template('articles.html', title=title, articles=articles)

@app.route('/tech')
def technology():
    '''
    View technology page function that returns the technology page and its data
    '''
    technology = get_articles_by_category_of_the_source('tech')
    title = 'Technology - News'
    return render_template('tech.html',title=title,technology=technology)
                           
                           
                           


