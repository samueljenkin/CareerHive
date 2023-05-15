from db.db import sql
import requests

def populate_db():
    api_url = 'https://apis.camillerakoto.fr/fakejobs/jobs'
    response = requests.get(api_url).json()
    for job in response:
        sql("INSERT INTO jobs(logo, title, salary, company, employment_type, city, zipcode, country, contact, content, date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) RETURNING *", [job['logo'], job['title'], 50000, job['name'], job['fulltime'], job['city'], job['zipcode'], job['country'], job['author'], job['content']])

def all_jobs():
    return sql("SELECT * FROM jobs ORDER BY id DESC")

def create_job(user_id, logo, title, salary, company, employment_type, city, zipcode, country, contact, content):
    sql("INSERT INTO jobs(user_id, logo, title, salary, company, employment_type, city, zipcode, country, contact, content, date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) RETURNING *", [user_id, logo, title, salary, company, employment_type, city, zipcode, country, contact, content])

def get_job(id):
    jobs = sql("SELECT * FROM jobs WHERE id=%s", [id])
    return jobs[0]

def update_job(logo, title, salary, company, employment_type, city, zipcode, country, contact, content, id):
    sql("UPDATE jobs SET logo=%s, title=%s, salary=%s, company=%s, employment_type=%s, city=%s, zipcode=%s, country=%s, contact=%s, content=%s WHERE id=%s RETURNING *", [logo, title, salary, company, employment_type, city, zipcode, country, contact, content, id])

def delete_job(id):
    sql("DELETE FROM jobs WHERE id=%s RETURNING *", [id])

def save_job(job_id, user_id):
    sql("INSERT INTO saved(job_id, user_id) VALUES(%s, %s) RETURNING *", [job_id, user_id])
    
def apply_to_job(job_id, user_id):
    sql("INSERT INTO applied(job_id, user_id) VALUES(%s, %s) RETURNING *", [job_id, user_id])

def report_job(job_id, user_id):
    sql("INSERT INTO reported(job_id, user_id) VALUES(%s, %s) RETURNING *", [job_id, user_id])

def view_job(job_id, user_id):
    sql("INSERT INTO viewed(job_id, user_id) VALUES(%s, %s) RETURNING *", [job_id, user_id])

def search_jobs(searched):
    jobs = sql("SELECT * FROM jobs WHERE title LIKE %s OR company LIKE %s OR city LIKE %s OR country LIKE %s", ['%' + searched + '%'] * 4)
    return jobs

def applied_jobs(user_id):
    jobs = sql("SELECT DISTINCT jobs.* FROM applied INNER JOIN jobs ON jobs.id = applied.job_id WHERE applied.user_id = %s ORDER BY id DESC", [user_id])
    return jobs

def saved_jobs(user_id):
    jobs = sql("SELECT DISTINCT jobs.* FROM saved INNER JOIN jobs ON jobs.id = saved.job_id WHERE saved.user_id = %s ORDER BY id DESC", [user_id])
    return jobs

def viewed_jobs(user_id):
    jobs = sql("SELECT DISTINCT jobs.* FROM viewed INNER JOIN jobs ON jobs.id = viewed.job_id WHERE viewed.user_id = %s ORDER BY id DESC", [user_id])
    return jobs

def reported_jobs(user_id):
    jobs = sql("SELECT DISTINCT jobs.* FROM reported INNER JOIN jobs ON jobs.id = reported.job_id WHERE reported.user_id = %s ORDER BY id DESC", [user_id])
    return jobs