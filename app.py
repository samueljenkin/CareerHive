from dotenv import dotenv_values
from flask import Flask, redirect
from routes.jobs_routes import jobs_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes

SECRETS = dotenv_values('.env')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRETS['SECRET_KEY']

app.register_blueprint(jobs_routes, url_prefix='/jobs')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

@app.route('/')
def index():
    return redirect('/jobs')