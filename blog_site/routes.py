from flask import Blueprint, render_template, redirect
from blog_site.forms import RegistrationForm
from blog_site.repositories import UsersRepository

main_routes = Blueprint('main', __name__, 'templates/')

@main_routes.route('/')
def index():
    return render_template('index.html', stuff="Hello!")

@main_routes.route('/sign-up', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        repo = UsersRepository()
        repo.register(
            form.email.data,
            form.first_name.data,
            form.last_name.data,
            form.password.data,
            form.username.data)
        return redirect('/')
    return render_template('register.html', register_form=form)

@main_routes.route('/success')
def success():
    return render_template('index.html', stuff="Thank you for registering.!")


@main_routes.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html')