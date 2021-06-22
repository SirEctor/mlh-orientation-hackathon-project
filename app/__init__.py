import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv
from . import db
from werkzeug.security import generate_password_hash
from app.db import get_db


load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

@app.route('/login')
def login_user():
    return render_template('index.html'), 200



app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
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
            return error, 418

    ## TODO: Return a restister page
    return "Register Page not yet implemented", 501


@app.route('/health')
def all_good():
    return render_template('index.html'), 200

@app.route('/')
def index():
    return render_template('index.html',  url=os.getenv("URL"))


