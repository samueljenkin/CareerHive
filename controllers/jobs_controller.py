from flask import render_template, request, redirect, session
from models.job import all_jobs

def index():
    jobs = all_jobs()
    return render_template('jobs/index.html', jobs=jobs)