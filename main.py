from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

class NameForm(FlaskForm):
    name = StringField("Username: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

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
