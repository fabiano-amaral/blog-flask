from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Fabiano'}
    posts = [
            {
                'Autor': {'nickname': 'Cesar'},
                'body': 'Um lindo dia no porto'
            },
            {
                'Autor': {'nickname': 'Bruno'},
                'body': 'Como matar seu professor, step by step'
            }
        ]
    return render_template(('index.html'),
                             title='Home',
                             user=user,
                             posts=posts)
