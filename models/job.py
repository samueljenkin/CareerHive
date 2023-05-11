from db.db import sql

def all_jobs():
    return sql('SELECT * FROM jobs ORDER BY id')

def create_job(title, salary, type, company, location, url, description):
    sql("INSERT INTO jobs(title, salary, type, company, location, url, description, date_posted) VALUES(%s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) RETURNING *", [title, salary, type, company, location, url, description])

def get_job(id):
    jobs = sql("SELECT * FROM jobs WHERE id=%s", [id])
    return jobs[0]

def update_job(title, salary, type, company, location, url, description, id):
    sql("UPDATE jobs SET title=%s, salary=%s, type=%s, company=%s, location=%s, url=%s, description=%s WHERE id=%s RETURNING *", [title, salary, type, company, location, url, description, id])

def delete_job(id):
    sql("DELETE FROM jobs WHERE id=%s RETURNING *", [id])

def save_job(job_id, user_id):
    sql("INSERT INTO saved(job_id, user_id) VALUES(%s, %s) RETURNING *", [job_id, user_id])