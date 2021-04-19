from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_articles, get_sources
from ..models import Source, Article


@main.route('/')
def index():
    title = 'Home: Welcome to the News Stand'
    sources = get_sources('sources?')
    return render_template('sources.html', title = title, sources= sources)

@main.route('/source/<name>')
def source_articles():
    title = f'{name}: Articles from {name}'
    articles = get_articles('top-headlines?country=us')
    return render_template('articles.html', title = title, articles= articles)

