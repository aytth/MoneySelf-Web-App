from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__, template_folder="templates")

@auth.route('/signup', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                # flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('success.html'))
            else:
                return redirect(url_for('home.html'))
        else:
            return redirect(url_for('home.html'))

    return render_template('signup.html', user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # Using the if statement to differentiate between GET and POST requests
    if (request.method=='POST'):
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(username=username).first()
        if user:
            return redirect(url_for('home.html'))
        elif (len(email)<4):
            return redirect(url_for('home.html'))
        elif (len(username)<3):
            return redirect(url_for('home.html'))
        elif (password1!=password2):
            return redirect(url_for('home.html'))
        elif (len(password1)<7):
            return redirect(url_for('home.html'))
        else:
            # Adds the user to the database
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1,
                method='sha256'
            ))
            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=True) # Logs in user once they have created the account
            # flash('Successfully signed up!', category='success')
            return redirect(url_for('home.html'))

    return render_template('signup.html', user=current_user)