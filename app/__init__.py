import os
from flask import Flask, render_template, send_from_directory, abort, request, redirect
from dotenv import load_dotenv
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db


load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

@app.route('/game/')
def game():
    return render_template('game.html')

@app.route('/contact/')
def contact():
    return redirect("https://http.cat/501")

@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/projects/')
def project():
    return render_template('projects.html')

@app.route('/health')
def all_good():
    return render_template('index.html'), 200

@app.route('/login/', methods=['GET', 'POST'])
def login():
    #return render_template('index.html'), 200
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful", 200 
        else:
            return error, 418
    
    ## tODO: Return a login page
    return render_template('login.html'), 200
    #return "Login Page not yet implemented", 501

    

@app.route('/register/',methods = ['POST', 'GET'])
def register():
    #return render_template('index.html'), 200
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return f"User {username} created successfully"
        else:
            return error,418
    return render_template('register.html'), 200
    #return "Register Page not yet implemented", 501
    ### tODO: Return a register page
 
@app.route('/')
def index():
    return render_template('index.html',  url=os.getenv("URL"))


