from flask import render_template, request, redirect, session
from models.job import populate_db, all_jobs, create_job, get_job, update_job, delete_job, save_job, apply_to_job, report_job, get_filtered_jobs
from services.session_info import current_user
import requests
    
def index():
    jobs = all_jobs()
    if jobs == []:
        populate_db()
        jobs = all_jobs()
    return render_template('jobs/index.html', jobs=jobs, current_user=current_user())

def new():
    return render_template('jobs/new.html')

def create():
    user_id = session['user_id']
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
    create_job(user_id, logo, title, salary, name, fulltime, city, zipcode, country, author, content)
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

def apply(id):
    apply_to_job(id, session['user_id'])
    return redirect('/')

def report(id):
    report_job(id, session['user_id'])
    return redirect('/')

def search():
    dropdown = request.form.get('dropdown')
    input = request.form.get('input')
    jobs = get_filtered_jobs(dropdown, input)
    return render_template('jobs/index.html', jobs=jobs, current_user=current_user())

def view(id):
    job = get_job(id)
    return render_template('jobs/view.html', job=job, current_user=current_user())