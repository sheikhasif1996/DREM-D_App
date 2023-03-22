from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET', 'POST'])
def login():
    user = {'name': 'Sheikh', 'age': 30}
    return render_template("login.html", user=user)

@auth.route('/logout')
def logout():
    user = {'name': 'Sheikh', 'age': 30}
    return "<p> Logout </p>"

@auth.route('/sign-up',methods=['GET', 'POST'])
def sign_up():
    user = {'name': 'Sheikh', 'age': 30}
    return render_template("sign-up.html", user=user)