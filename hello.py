from flask import Flask
from flask import request
app = Flask(__name__)

import time
import requests
import jwt

jwt_key = 'secret'
# count=0
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route("/echo",methods=['GET'])
# def echo():
#     name=request.args.get('name')
#     return 'Hello{}'.format(name)
#
# @app.route("/count",methods=['GET'])
# def counter():
#     global count
#     count+=1
#     return 'the no of times called:{}'.format(count)

@app.route("/timer",methods=['GET'])
def timer():
        start_time = time.time()*1000
        url=request.args.get('url')
        requests.get(url)
        end_time = time.time()*1000
        return "time taken {}".format(end_time - start_time)

@app.route('/fetch_access',methods=['GET'])
def get_access():
        global jwt_key
        url = request.args.get('url')
        perms = request.args.get('perms')

        payload={
        'url':url,
         'perms':perms

        }
        token=jwt.encode(payload,jwt_key,algorithm='HS256')
        return token;

@app.route('/check_access',methods=['GET'])
def check_access():
        token = request.args.get('access_token')
        payload=jwt.decode(token,jwt_key)
        return payload

if __name__ == '__main__':
    app.run(port='5004',debug=True)

