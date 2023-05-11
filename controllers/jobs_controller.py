from flask import render_template, request, redirect, session
from models.job import all_jobs, create_job, get_job, update_job, delete_job, save_job

def index():
    jobs = all_jobs()
    return render_template('jobs/index.html', jobs=jobs)

def new():
    return render_template('jobs/new.html')

def create():
    title = request.form.get('title')
    salary = request.form.get('salary')
    type = request.form.get('type')
    company = request.form.get('company')
    location = request.form.get('location')
    url = request.form.get('url')
    description = request.form.get('description')
    create_job(title, salary, type, company, location, url, description)
    return redirect('/')

def edit(id):
    job = get_job(id)
    return render_template('jobs/edit.html', job=job)

def update(id):
    title = request.form.get('title')
    salary = request.form.get('salary')
    type = request.form.get('type')
    company = request.form.get('company')
    location = request.form.get('location')
    url = request.form.get('url')
    description = request.form.get('description')
    update_job(title, salary, type, company, location, url, description, id)
    return redirect('/')

def delete(id):
    delete_job(id)
    return redirect('/')

def save(id):
    save_job(id, session['user_id'])
    return redirect('/')