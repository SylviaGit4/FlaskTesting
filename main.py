from flask import Flask, url_for, render_template, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir + 'data.sqlite')
db = SQLAlchemy(app)

class NameForm(FlaskForm):
    name = StringField("Username: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)

with app.app_context():
    db.create_all()

items = ["Item 1", "Item 2", "Item 3"]

username = "USER"

@app.route('/', methods = ['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    if name == username:
        return redirect(f'/user/{name}')

    return render_template('index.html', form=form, name=name, items = items)

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username = username)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
