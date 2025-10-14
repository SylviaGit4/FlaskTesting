from flask import Flask, render_template

app = Flask(__name__)

name = "user"
items = ["Item 1", "Item 2", "Item 3"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

@app.route('/list')
def list():
    return render_template('list.html', items = items)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
