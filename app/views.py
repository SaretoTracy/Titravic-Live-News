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