from flask import render_template
from . import main

@main.app_errorhandler(404)
def four0four(error):
    return render_tempate('404.html'),404