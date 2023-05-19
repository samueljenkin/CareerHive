from flask import render_template, request, redirect, session
from models.job import populate_db, all_jobs, create_job, get_job, update_job, delete_job, save_job, apply_to_job, report_job, view_job, advanced_search, applied_jobs, saved_jobs, viewed_jobs, reported_jobs, remove_report, search_jobs
from services.session_info import current_user
    
def index():
    jobs = all_jobs()
    if jobs == []:
        populate_db()
        jobs = all_jobs()
    return render_template('jobs/index.html', jobs=jobs, current_user=current_user())

def new():
    return render_template('jobs/new.html', current_user=current_user())

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
    description = request.form.get('description')
    create_job(user_id, logo, title, salary, company, employment_type, city, zipcode, country, contact, description)
    return redirect('/')

def edit(id):
    job = get_job(id)
    view_mode = request.args.get('view')
    return render_template('jobs/edit.html', job=job, view_mode=view_mode, current_user=current_user())

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
    description = request.form.get('description')
    update_job(logo, title, salary, company, employment_type, city, zipcode, country, contact, description, id)
    view_mode = request.args.get('view')
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
    stored_type = request.args.get('stored')
    if view_mode == 'True':
        return redirect(f'/jobs/{id}/view')
    elif stored_type:
        return stored()
    else:
        return redirect('/')

def apply(id):
    apply_to_job(id, session['user_id'])
    view_mode = request.args.get('view')
    stored_type = request.args.get('stored')
    if view_mode == 'True':
        return redirect(f'/jobs/{id}/view')
    elif stored_type:
        return stored()
    else:
        return redirect('/')

def report(id):
    return render_template('jobs/report.html', id=id, current_user=current_user())

def file(id):
    message = request.form.get('message')
    report_job(id, session['user_id'], message)
    view_mode = request.args.get('view')
    stored_type = request.args.get('stored')
    if view_mode == 'True':
        return redirect(f'/jobs/{id}/view')
    elif stored_type:
        return stored()
    else:
        return redirect('/')

def search():
    search = True
    what = request.form.get('what')
    where = request.form.get('where')
    employment_type = request.form.get('employment_type')
    salary = request.form.get('salary')
    advanced = request.form.get('advanced')
    if advanced == 'True':
        advanced = True
    if not employment_type and not salary:
        jobs = search_jobs(what.capitalize(), where.capitalize())
    else:
        jobs = advanced_search(what.capitalize(), where.capitalize(), employment_type, salary.split())
    return render_template('jobs/index.html', advanced=advanced, search=search, jobs=jobs, current_user=current_user())

def advanced():
    advanced = True
    jobs = all_jobs()
    return render_template('jobs/index.html', jobs=jobs, advanced=advanced, current_user=current_user())

def view(id):
    view_job(id, session['user_id'])
    job = get_job(id)
    return render_template('jobs/view.html', job=job, current_user=current_user())

def stored():
    stored_type = request.args.get('stored')
    print(stored_type)
    print(stored_type)
    if stored_type == 'applied':
        jobs = applied_jobs(session['user_id'])
    elif stored_type == 'saved':
        jobs = saved_jobs(session['user_id'])
    elif stored_type == 'viewed':
        jobs = viewed_jobs(session['user_id'])
    elif stored_type == 'reported':
        jobs = reported_jobs(session['user_id'])
    return render_template('jobs/stored.html', stored_type=stored_type, jobs=jobs, current_user=current_user())

def remove(id):
    remove_report(id)
    return stored()