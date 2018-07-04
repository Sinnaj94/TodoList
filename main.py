from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/categories', methods=['GET', 'POST'])
def categories():
    return 'TODO'

@app.route('/tasks')
def tasks():
    return render_template('tasks.html', tasks = ['a', 'b', 'c'])



if __name__ == '__main__':
    app.run(debug=True)
