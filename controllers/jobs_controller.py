from flask import render_template, request, redirect, session
from models.job import populate_db, all_jobs, create_job, get_job, update_job, delete_job, save_job, apply_to_job, report_job, view_job, search_jobs, applied_jobs, saved_jobs, viewed_jobs, reported_jobs
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
    company = request.form.get('company')
    employment_type = request.form.get('employment_type')
    city = request.form.get('city')
    zipcode = request.form.get('zipcode')
    country = request.form.get('country')
    contact = request.form.get('contact')
    content = request.form.get('content')
    create_job(user_id, logo, title, salary, company, employment_type, city, zipcode, country, contact, content)
    return redirect('/')

def edit(id):
    job = get_job(id)
    view_mode = request.args.get('view')
    print(view_mode)
    return render_template('jobs/edit.html', job=job, view_mode=view_mode)

def update(id):
    logo = request.form.get('logo')
    title = request.form.get('title')
    salary = request.form.get('salary')
    company = request.form.get('company')
    employment_type = request.form.get('employment_type')
    city = request.form.get('city')
    zipcode = request.form.get('zipcode')
    country = request.form.get('country')
    contact = request.form.get('contact')
    content = request.form.get('content')
    update_job(logo, title, salary, company, employment_type, city, zipcode, country, contact, content, id)
    view_mode = request.args.get('view')
    print(view_mode)
    if view_mode == 'True':
        return redirect(f'/jobs/{id}/view')
    else:
        return redirect('/')

def delete(id):
    delete_job(id)
    return redirect('/')

def save(id):
    save_job(id, session['user_id'])
    view_mode = request.args.get('view')
    if view_mode == 'True':
        return redirect(f'/jobs/{id}/view')
    else:
        return redirect('/')

def apply(id):
    apply_to_job(id, session['user_id'])
    view_mode = request.args.get('view')
    if view_mode == 'True':
        return redirect(f'/jobs/{id}/view')
    else:
        return redirect('/')

def report(id):
    report_job(id, session['user_id'])
    view_mode = request.args.get('view')
    if view_mode == 'True':
        return redirect(f'/jobs/{id}/view')
    else:
        return redirect('/')

def search():
    searched = request.form.get('searched')
    jobs = search_jobs(searched)
    return render_template('jobs/index.html', jobs=jobs, current_user=current_user())

def view(id):
    view_job(id, session['user_id'])
    job = get_job(id)
    return render_template('jobs/view.html', job=job, current_user=current_user())

def stored():
    stored_type = request.args.get('stored')
    if stored_type == 'applied':
        jobs = applied_jobs(session['user_id'])
    elif stored_type == 'saved':
        jobs = saved_jobs(session['user_id'])
    elif stored_type == 'viewed':
        jobs = viewed_jobs(session['user_id'])
    elif stored_type == 'reported':
        jobs = reported_jobs(session['user_id'])
    return render_template('jobs/stored.html', stored_type=stored_type, jobs=jobs)