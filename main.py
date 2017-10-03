from flask import Flask, request
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


@app.route('/')
def display_signup():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route('/', methods=['POST'])
def validate_input():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email= request.form['email']

    username_error=''
    password_error=''
    verify_password_error=''
    email_error=''

    if len(username)<3 or len(username)>20 or " " in username:
        username_error='Please enter a valid username'

    if len(password)<3 or len(password)>20 or " " in password:
        password_error='Please enter a valid password'

    if password != verify_password:
        verify_password_error= 'Please enter a matching password'

    if len(email)>1 and ("@" not in email or "."  not in email):
        email_error='Please enter a valid email or leave blank'

    if not username_error and not password_error and not verify_password_error and not email_error:
        return "Welcome, "+ username+"!"
    else:
        template = jinja_env.get_template('form.html')
        return template.render(username_error=username_error, password_error=password_error,verify_password_error=verify_password_error,email_error=email_error,username=username,password="",verify_password="",email=email)

app.run()
