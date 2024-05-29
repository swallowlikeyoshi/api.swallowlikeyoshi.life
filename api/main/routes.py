from flask import render_template
from . import main

@main.route('/')
def index():
    return "lasciate ogni speranza, voi ch'entrate"
    # return render_template('index.html')

@main.route('/robots.txt')
def robots():
    return "User-agent: * Disallow: *"