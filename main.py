from flask import Flask
from flask import request, g, jsonify, abort
from flask import render_template
import data
import datetime
# TODO: Implement getter and setter, connect with data.py
app = Flask(__name__)
# TODO: Echte variablen


@app.route('/')
def hello_world():
    return render_template('index.html')


# TODO: Oguzhan: GET und POST implementieren (mit Nutzung von data.py)
@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'POST':
        category_name = request.form['category_name']
        data.add_category(category_name)
    t = data.get_category()
    return render_template('categories.html', categories=t)


# TODO: David: GET und POST implementieren (mit Nutzung von data.py)
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        important = 0
        if 'important' in request.form:
            important = 1
        category = None
        if request.form['category'] != -1:
            category = request.form['category']

        date = datetime.datetime.strptime(request.form['due_date'], "%Y-%m-%d")
        data.add_task(request.form['description'], date.strftime("%d.%m.%Y"), important, category)

    t = data.get_tasks()
    c = data.get_category()
    return render_template('tasks.html', tasks=t, categories=c)


# TODO: Jannis: GET, DELETE und PUT implementieren
@app.route('/tasks/<id>', methods=['GET', 'PUT', 'DELETE'])
def task(id):
    t = data.get_task_by_id(id)
    if(len(t) == 0):
        return abort(404)
    elif request.method == 'DELETE':
        data.remove_task(id)
    elif request.method == 'PUT':
        t = data.update_task(id, request.form)
    return jsonify(task=t[0], method=request.method)




# TODO: Jannis: GET, DELETE und PUT implementieren
@app.route('/categories/<id>', methods=['GET', 'DELETE', 'PUT'])
def category(id):
    c = data.get_category()
    if request.method == 'DELETE':
        data.remove_category(id)
    return jsonify(category=c[0], method=request.method)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=404, text="The requested resource was not found."), 404


if __name__ == '__main__':
    app.run(debug=True)
