from db.db import sql
import requests

def populate_db():
    api_url = 'https://apis.camillerakoto.fr/fakejobs/jobs'
    response = requests.get(api_url).json()
    employment_type = ''
    for job in response:
        if job['fulltime'] == 'true':
            employment_type = 'full-time'
        else:
            employment_type = 'part-time'
        sql("INSERT INTO jobs(logo, title, salary, company, employment_type, city, zipcode, country, contact, description, date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) RETURNING *", [job['logo'], job['title'], 50000, job['name'], employment_type, job['city'], job['zipcode'], job['country'], job['author'], job['content']])

def all_jobs():
    return sql("SELECT * FROM jobs ORDER BY id DESC")

def create_job(user_id, logo, title, salary, company, employment_type, city, zipcode, country, contact, description):
    sql("INSERT INTO jobs(user_id, logo, title, salary, company, employment_type, city, zipcode, country, contact, description, date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) RETURNING *", [user_id, logo, title, salary, company, employment_type, city, zipcode, country, contact, description])

def get_job(id):
    jobs = sql("SELECT * FROM jobs WHERE id=%s", [id])
    return jobs[0]

def update_job(logo, title, salary, company, employment_type, city, zipcode, country, contact, description, id):
    sql("UPDATE jobs SET logo=%s, title=%s, salary=%s, company=%s, employment_type=%s, city=%s, zipcode=%s, country=%s, contact=%s, description=%s WHERE id=%s RETURNING *", [logo, title, salary, company, employment_type, city, zipcode, country, contact, description, id])

def delete_job(id):
    sql("DELETE FROM jobs WHERE id=%s RETURNING *", [id])

def save_job(job_id, user_id):
    sql("INSERT INTO saved(job_id, user_id) VALUES(%s, %s) RETURNING *", [job_id, user_id])
    
def apply_to_job(job_id, user_id):
    sql("INSERT INTO applied(job_id, user_id) VALUES(%s, %s) RETURNING *", [job_id, user_id])

def report_job(job_id, user_id, message):
    sql("INSERT INTO reported(job_id, user_id, message, date) VALUES(%s, %s, %s, CURRENT_TIMESTAMP) RETURNING *", [job_id, user_id, message])

def view_job(job_id, user_id):
    sql("INSERT INTO viewed(job_id, user_id) VALUES(%s, %s) RETURNING *", [job_id, user_id])

def search_jobs(searched, employment_type, salary):
    if searched == '' and employment_type == 'None' and salary[0] == 'None':
        jobs = sql("SELECT * FROM jobs ORDER BY id DESC")
    elif searched == '' and employment_type != 'None' and salary[0] == 'None':
        jobs = sql("SELECT * FROM jobs WHERE employment_type=%s ORDER BY id DESC", [employment_type])
    elif searched == '' and employment_type == 'None' and salary[0] != 'None':
        jobs = sql("SELECT * FROM jobs WHERE salary BETWEEN %s AND %s ORDER BY id DESC", [int(salary[0]), int(salary[1])])
    elif searched == '' and employment_type != 'None' and salary[0] != 'None':
        jobs = sql("SELECT * FROM jobs WHERE employment_type=%s AND salary BETWEEN %s AND %s ORDER BY id DESC", [employment_type, int(salary[0]), int(salary[1])])
    elif searched != '' and employment_type == 'None' and salary[0] == 'None':
        jobs = sql("SELECT * FROM jobs WHERE title ILIKE %s OR company ILIKE %s OR city ILIKE %s OR country ILIKE %s ORDER BY id DESC", ['%' + searched + '%'] * 4)
    elif searched != '' and employment_type != 'None' and salary[0] == 'None':
        jobs = sql("SELECT * FROM jobs WHERE employment_type=%s OR title ILIKE %s OR company ILIKE %s OR city ILIKE %s OR country ILIKE %s ORDER BY id DESC", [employment_type, '%' + searched + '%', '%' + searched + '%', '%' + searched + '%', '%' + searched + '%'])
    elif searched != '' and employment_type == 'None' and salary[0] != 'None':
        jobs = sql("SELECT * FROM jobs WHERE salary BETWEEN %s AND %s OR title ILIKE %s OR company ILIKE %s OR city ILIKE %s OR country ILIKE %s ORDER BY id DESC", [int(salary[0]), int(salary[1]), '%' + searched + '%', '%' + searched + '%', '%' + searched + '%', '%' + searched + '%'])
    elif searched != '' and employment_type != 'None' and salary[0] != 'None':
        jobs = sql("SELECT * FROM jobs WHERE employment_type=%s AND salary BETWEEN %s AND %s OR title ILIKE %s OR company ILIKE %s OR city ILIKE %s OR country ILIKE %s ORDER BY id DESC", [employment_type, int(salary[0]), int(salary[1]), '%' + searched + '%', '%' + searched + '%', '%' + searched + '%', '%' + searched + '%'])
    return jobs

def applied_jobs(user_id):
    jobs = sql("SELECT jobs.*, MAX(applied.id) AS applied_id FROM applied INNER JOIN jobs ON jobs.id = applied.job_id WHERE applied.user_id=%s GROUP BY jobs.id ORDER BY applied_id DESC", [user_id])
    return jobs

def saved_jobs(user_id):
    jobs = sql("SELECT jobs.*, MAX(saved.id) AS saved_id FROM saved INNER JOIN jobs ON jobs.id = saved.job_id WHERE saved.user_id=%s GROUP BY jobs.id ORDER BY saved_id DESC", [user_id])
    return jobs

def viewed_jobs(user_id):
    jobs = sql("SELECT jobs.*, MAX(viewed.id) AS viewed_id FROM viewed INNER JOIN jobs ON jobs.id = viewed.job_id WHERE viewed.user_id=%s GROUP BY jobs.id ORDER BY viewed_id DESC", [user_id])
    return jobs

def reported_jobs(user_id):
    jobs = sql("SELECT jobs.*, reported.message FROM jobs INNER JOIN reported ON jobs.id = reported.job_id WHERE reported.id IN (SELECT MAX(id) FROM reported WHERE user_id=%s GROUP BY job_id) ORDER BY reported.id DESC", [user_id])
    return jobs

def remove_report(id):
    sql("DELETE FROM reported WHERE job_id=%s RETURNING *", [id])