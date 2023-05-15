from db.db import sql
import requests

def populate_db():
    api_url = 'https://apis.camillerakoto.fr/fakejobs/jobs'
    response = requests.get(api_url).json()
    for job in response:
        sql("INSERT INTO jobs(logo, title, salary, name, fulltime, city, zipcode, country, author, content, date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) RETURNING *", [job['logo'], job['title'], job['salary'], job['name'], job['fulltime'], job['city'], job['zipcode'], job['country'], job['author'], job['content']])

def all_jobs():
    return sql('SELECT * FROM jobs ORDER BY id')

def create_job(user_id, logo, title, salary, name, fulltime, city, zipcode, country, author, content):
    sql("INSERT INTO jobs(user_id, logo, title, salary, name, fulltime, city, zipcode, country, author, content, date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) RETURNING *", [user_id, logo, title, salary, name, fulltime, city, zipcode, country, author, content])

def get_job(id):
    jobs = sql("SELECT * FROM jobs WHERE id=%s", [id])
    return jobs[0]

def update_job(logo, title, salary, name, fulltime, city, zipcode, country, author, content, id):
    sql("UPDATE jobs SET logo=%s, title=%s, salary=%s, name=%s, fulltime=%s, city=%s, zipcode=%s, country=%s, author=%s, content=%s WHERE id=%s RETURNING *", [logo, title, salary, name, fulltime, city, zipcode, country, author, content, id])

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

def get_filtered_jobs(dropdown, input):
    jobs = sql(f"SELECT * FROM jobs WHERE {dropdown}='{input}'")
    return jobs

def applied_jobs(user_id):
    jobs = sql("SELECT DISTINCT jobs.* FROM applied INNER JOIN jobs ON jobs.id = applied.job_id WHERE applied.user_id = %s", [user_id])
    return jobs