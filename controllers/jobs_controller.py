from flask import render_template, request, redirect, session
from models.job import all_jobs, create_job, get_job, update_job, delete_job, save_job
from services.session_info import current_user
import requests

def get_all_jobs_from_api():
    api_url = 'https://apis.camillerakoto.fr/fakejobs/jobs'
    response = requests.get(api_url).json()
    return response

def get_filtered_jobs_from_api(key, value):
    api_url = f'https://apis.camillerakoto.fr/fakejobs/jobs?{key}={value}'
    response = requests.get(api_url).json()
    return response
    
def index():
    jobs = all_jobs()
    api_jobs = get_all_jobs_from_api()
    key = request.form.get('key')
    value = request.form.get('value')
    filtered_api_jobs = get_filtered_jobs_from_api(key, value)
    if value == None:
        return render_template('jobs/index.html', jobs=jobs, api_jobs=api_jobs, current_user=current_user())
    else:
        return render_template('jobs/index.html', jobs=jobs, api_jobs=filtered_api_jobs, current_user=current_user())

def new():
    return render_template('jobs/new.html')

def create():
    logo = request.form.get('logo')
    title = request.form.get('title')
    salary = request.form.get('salary')
    name = request.form.get('name')
    fulltime = request.form.get('fulltime')
    city = request.form.get('city')
    zipcode = request.form.get('zipcode')
    country = request.form.get('country')
    author = request.form.get('author')
    content = request.form.get('content')
    create_job(logo, title, salary, name, fulltime, city, zipcode, country, author, content)
    return redirect('/')

def edit(id):
    job = get_job(id)
    return render_template('jobs/edit.html', job=job)

def update(id):
    logo = request.form.get('logo')
    title = request.form.get('title')
    salary = request.form.get('salary')
    name = request.form.get('name')
    fulltime = request.form.get('fulltime')
    city = request.form.get('city')
    zipcode = request.form.get('zipcode')
    country = request.form.get('country')
    author = request.form.get('author')
    content = request.form.get('content')
    update_job(logo, title, salary, name, fulltime, city, zipcode, country, author, content, id)
    return redirect('/')

def delete(id):
    delete_job(id)
    return redirect('/')

def save(id):
    save_job(id, session['user_id'])
    return redirect('/')