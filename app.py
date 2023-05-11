from flask import Flask, redirect
from routes.jobs_routes import jobs_routes
from routes.users_routes import users_routes

app = Flask(__name__)

app.register_blueprint(jobs_routes, url_prefix='/jobs')
app.register_blueprint(users_routes, url_prefix='/users')

@app.route('/')
def index():
    return redirect('/jobs')