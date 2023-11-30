from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from . import auth_bp
from .models import User
from .forms import RegistrationForm, LoginForm

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logged in successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)
