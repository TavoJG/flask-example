from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/json")
def json_response():
    return {
        'code': 200,
        'data': 'Soy una respuesta JSON',
        'boolean': False
    }


@app.route("/http_methods")
def http_methods():
    if not request.method in ['POST', 'PUT', 'PATCH']:
        return request.method
    body = request.get_json()
    return jsonify(body)


@app.route("/url_params/<param>")
def url_param(param):
    return param


@app.route('/template/')
@app.route('/template/<name>')
def name_template(name=None):
    print(name)
    return render_template('hello.html', name=name)
