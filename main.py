from flask import Flask
from flask import request, g, jsonify, abort
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
    if request.method == 'POST':
        category_name = request.form['cat_input'] #form input name
        t = data.add_category(category_name)
        #TODO was hier zurückgeben?
    else:
        t = data.get_category()
        return render_template('categories.html', categories=t)


# TODO: David: GET und POST implementieren (mit Nutzung von data.py)
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    t = data.get_tasks()
    return render_template('tasks.html', tasks=t)


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
    return 'TODO'


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=404, text="The requested resource was not found."), 404


if __name__ == '__main__':
    app.run(debug=True)
