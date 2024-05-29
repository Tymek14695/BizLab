from app import app
from flask import render_template, request, redirect, url_for
from app.scripts.models import *




@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


'''@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f'Login requested for user {form.username.data}.')'''


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    print('xd')
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        retypePassword = request.form.get('retypePassword')
    return render_template('register.html')


@app.route('/redirect')



SMACONT = 'container-sm p-1 text-primary-emphasis bg-primary-subtle border border-primary-subtle rounded-0'
MEDCONT = 'container-md p-3 text-primary-emphasis bg-primary-subtle border border-primary-subtle rounded-0'
BIGCONT = 'container-l p-5 text-primary-emphasis bg-primary-subtle border border-primary-subtle rounded-0'

ERRCONT = 'container-sm p-5 text-error-emphasis bg-error-subtle border border-error-subtle rounded-5'
WARCONT = 'container-sm p-5 text-warning-emphasis bg-warning-subtle border border-warning-subtle rounded-5'
SUCCONT = 'container-sm p-5 text-success-emphasis bg-success-subtle border border-success-subtle rounded-5'
INFCONT = 'container-sm p-5 text-info-emphasis bg-info-subtle border border-info-subtle rounded-5'