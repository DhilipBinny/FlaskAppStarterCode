import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PORT = int(os.getenv("PORT", 5000))

@app.route("/")
def hello():
    return "Hello World!"

# POST with query params
@app.route('/login', methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username,password)
    return jsonify({"user":username, "pass":password})

# form POST
@app.route('/form_login', methods=['POST'])
def form_login():
    username = request.form.get('username')
    password= request.form.get('password')
    return jsonify({"user":username, "pass":password})

# GET with default params and datatypes
@app.route('/pages')
def pages():
  page_ = request.args.get('page', default = 1, type = int)
  filter_ = request.args.get('filter', default = '*', type = str)
  print(page_,filter_)
  return jsonify({"page":page_, "filter":filter_})

# GET with path param
@app.route('/path/<param>')
def pathparam(param):
    return param

# GET with datatype specified path param
@app.route('/path2/<int:param>/')
def pathparam_withdatatype(param):
    return  str(param)

# post raw data  with headers Content-Type: application/json
@app.route('/json', methods=['POST']) 
def raw():
    print(request.data)
    data = request.json
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=PORT)