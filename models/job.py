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
        jobs = sql("SELECT * FROM jobs WHERE title LIKE %s OR company LIKE %s OR city LIKE %s OR country LIKE %s ORDER BY id DESC", ['%' + searched + '%'] * 4)
    elif searched != '' and employment_type != 'None' and salary[0] == 'None':
        jobs = sql("SELECT * FROM jobs WHERE employment_type=%s OR title LIKE %s OR company LIKE %s OR city LIKE %s OR country LIKE %s ORDER BY id DESC", [employment_type, '%' + searched + '%', '%' + searched + '%', '%' + searched + '%', '%' + searched + '%'])
    elif searched != '' and employment_type == 'None' and salary[0] != 'None':
        jobs = sql("SELECT * FROM jobs WHERE salary BETWEEN %s AND %s OR title LIKE %s OR company LIKE %s OR city LIKE %s OR country LIKE %s ORDER BY id DESC", [int(salary[0]), int(salary[1]), '%' + searched + '%', '%' + searched + '%', '%' + searched + '%', '%' + searched + '%'])
    elif searched != '' and employment_type != 'None' and salary[0] != 'None':
        jobs = sql("SELECT * FROM jobs WHERE employment_type=%s AND salary BETWEEN %s AND %s OR title LIKE %s OR company LIKE %s OR city LIKE %s OR country LIKE %s ORDER BY id DESC", [employment_type, int(salary[0]), int(salary[1]), '%' + searched + '%', '%' + searched + '%', '%' + searched + '%', '%' + searched + '%'])
    return jobs

def applied_jobs(user_id):
    jobs = sql("SELECT jobs.*, MAX(applied.id) AS applied_id FROM applied INNER JOIN jobs ON jobs.id = applied.job_id WHERE applied.user_id = %s GROUP BY jobs.id ORDER BY applied_id DESC", [user_id])
    return jobs

def saved_jobs(user_id):
    jobs = sql("SELECT jobs.*, MAX(saved.id) AS saved_id FROM saved INNER JOIN jobs ON jobs.id = saved.job_id WHERE saved.user_id = %s GROUP BY jobs.id ORDER BY saved_id DESC", [user_id])
    return jobs

def viewed_jobs(user_id):
    jobs = sql("SELECT jobs.*, MAX(viewed.id) AS viewed_id FROM viewed INNER JOIN jobs ON jobs.id = viewed.job_id WHERE viewed.user_id = %s GROUP BY jobs.id ORDER BY viewed_id DESCC", [user_id])
    return jobs

def reported_jobs(user_id):
    jobs = sql("SELECT jobs.*, MAX(reported.id) AS reported_id FROM reported INNER JOIN jobs ON jobs.id = reported.job_id WHERE reported.user_id = %s GROUP BY jobs.id ORDER BY reported_id DESC", [user_id])
    return jobs