from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
@app.route('/contato')
def contato():
    return render_template('contato.html')