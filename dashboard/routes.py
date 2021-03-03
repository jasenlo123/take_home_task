from flask import render_template, url_for, flash, redirect, request
from dashboard import app, db, bcrypt
from dashboard.forms import LoginForm
from dashboard.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required



posts = [
    {
        'author': 'Konti Tester',
        'title': 'Blog Post 1',
        'content': 'post content',
        'date_posted': "yesterday"
    },
    {
        'author': 'Konti Tester 2',
        'title': 'Blog Post 2',
        'content': 'more content',
        'date_posted': "yesterday"

    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html',posts= posts)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))