from flask import Blueprint, render_template
from blog_site.forms import RegistrationForm

main_routes = Blueprint('main', __name__, 'templates/')

@main_routes.route('/')
def index():
    return render_template('index.html', stuff="Hello!")

@main_routes.route('/sign-up', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)