import os
from dotenv import load_dotenv
from flask import Flask, redirect
from routes.jobs_routes import jobs_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

app.register_blueprint(jobs_routes, url_prefix='/jobs')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

@app.route('/')
def index():
    return redirect('/jobs')