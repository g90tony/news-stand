from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_articles, get_sources
from ..models import Source, Article


@main.route('/')
def index():
    title = 'Home: Welcome to the News Stand'
    sources = get_sources()
    return render_template('sources.html', title = title, sources= sources)

@main.route('/source/<query_term>')
def source_articles(query_term):
    title = f'{query_term}: Articles from {query_term}'
    articles = get_articles(f'everything?sources={query_term}&')
    return render_template('articles.html', title = title, articles= articles)

