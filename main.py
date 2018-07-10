from flask import Flask
from flask import request, g
from flask import render_template
import data
# TODO: Implement getter and setter, connect with data.py
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/categories', methods=['GET', 'POST'])
def categories():
    return 'TODO'


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    return render_template('tasks.html', tasks = ['a', 'b', 'c'])


if __name__ == '__main__':
    app.run(debug=True)
