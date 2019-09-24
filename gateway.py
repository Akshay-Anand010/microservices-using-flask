from flask import Flask
from flask import request
from logger import root
app = Flask(__name__)
jwt_key = 'secret'
import time
import requests
import jwt
access_provider_url='http://localhost:5004'
access_counter_url='http://localhost:5002'
@app.route('/v1/access',methods=['GET'])
def access():



  @app.route("/count",methods=['GET'])
def counter():
    global count
    count+=1
    return count



if __name__ == '__main__':
    app.run(port='5001',debug=True)
