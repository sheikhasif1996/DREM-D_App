from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    user = {'name': 'Sheikh', 'age': 30}
    return render_template("home.html", user=user)