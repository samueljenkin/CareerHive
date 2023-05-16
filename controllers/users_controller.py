from flask import render_template, request, redirect, session
from models.user import create_user, find_user_by_email

def new():
    return render_template('users/new.html')

def create():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    create_user(first_name, last_name, email, password)
    user = find_user_by_email(email)
    session['user_id'] = user['id']
    return redirect('/')