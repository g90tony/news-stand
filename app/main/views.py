from flask import render_template, request, redirect, url_for
from . import main
from ..models import Source, Article


@main.route('/')
def index():
    title = 'Home: Welcome to the News Stand'
    return render_template('home.html', title = title)