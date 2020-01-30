from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'LoTek'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in NYC!'
        },
        {
            'author': {'username': 'Haley'},
            'body': 'So excited about the superbowl!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)