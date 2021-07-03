import os
from flask import Flask, render_template, send_from_directory, abort, request, redirect
#from dotenv import load_dotenv
#from . import db
from werkzeug.security import generate_password_hash, check_password_hash
#from app.db import get_db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#load_dotenv()
app = Flask(__name__)
#app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
#db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}'.format(
	user=os.getenv('POSTGRES_USER'),
        passwd=os.getenv('POSTGRES_PASSWORD'),
	host=os.getenv('POSTGRES_HOST'),
	port=5432,
	table=os.getenv('POSTGRES_DB'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UserModel(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"


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
        error = None
        user = UserModel.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful", 200 
        else:
            return error, 418
    
    ## tODO: Return a login page
    return render_template('login.html'), 200
    #return "Login Page not yet implemented", 501

    

@app.route('/register/', methods = ['POST', 'GET'])
def register():
    #return render_template('index.html'), 200
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif UserModel.query.filter_by(username=username).first() is not None:
            error = f"User {username} is already registered."

        if error is None:
            new_user =  UserModel(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return f"User {username} created successfully"
        else:
            return error,418
    return render_template('register.html'), 200
    #return "Register Page not yet implemented", 501
    ### tODO: Return a register page
 
@app.route('/')
def index():
    return render_template('index.html',  url=os.getenv("URL"))


