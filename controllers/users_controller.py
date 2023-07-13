from flask import render_template, request, redirect, session
from models.user import create_user, find_user_by_email

def new():
    return render_template('users/new.html')

def create():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    create_user(username, email, password)
    user = find_user_by_email(email)
    session['user_id'] = user['id']
    return redirect('/')