from flask import Flask, redirect
from routes.jobs_routes import jobs_routes

app = Flask(__name__)

app.register_blueprint(jobs_routes, url_prefix='/jobs')

@app.route('/')
def index():
    return redirect('/jobs')