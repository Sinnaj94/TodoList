from flask import Flask
from flask import request, g
from flask import render_template
import data
# TODO: Implement getter and setter, connect with data.py
app = Flask(__name__)
# TODO: Echte variablen


@app.route('/')
def hello_world():
    return render_template('index.html')


# TODO: Oguzhan: GET und POST implementieren (mit Nutzung von data.py)
@app.route('/categories', methods=['GET', 'POST'])
def categories():
    return 'TODO'


# TODO: David: GET und POST implementieren (mit Nutzung von data.py)
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    t = data.get_tasks()
    return render_template('tasks.html', tasks=t)


# TODO: Jannis: GET, DELETE und PUT implementieren
@app.route('/tasks/<id>')
def task(id):
    return 'TODO'


# TODO: Jannis: GET, DELETE und PUT implementieren
@app.route('/categories/<id>', methods=['GET', 'DELETE', 'PUT'])
def category(id):
    return 'TODO'


if __name__ == '__main__':
    app.run(debug=True)
