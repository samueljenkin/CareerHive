from db.db import sql
import bcrypt

def create_user(first_name, last_name, email, password):
    password_digest = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql("INSERT INTO users(first_name, last_name, email, password_digest) VALUES(%s, %s, %s, %s) RETURNING *", [first_name, last_name, email, password_digest])