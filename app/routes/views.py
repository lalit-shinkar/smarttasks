from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return render_template('index.html')

@main_routes.route('/add')
def add_task():
    return render_template('add_task.html')

