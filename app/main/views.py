from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_articles, get_sources
from ..models import Source, Article


@main.route('/')
def index():
    title = 'Home: Welcome to the News Stand'
    sources = get_sources('sources?')
    return render_template('sources.html', title = title, sources= sources)

