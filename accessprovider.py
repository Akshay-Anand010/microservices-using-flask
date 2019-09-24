
from flask import Flask
from flask import request
from logger import root
app = Flask(__name__)

import time
import requests
import jwt
jwt_key='bnmit'



@app.route('/fetch_access',methods=['GET'])
def get_access():
    global jwt_key

    url = request.args.get('url')
    perms = request.args.get('perms')
    user_id = request.args.get('user_id')
    user_access = {
            "1": ["http://google.com", "http://facebook.com"],
            "2": ["http://google.com"]
        }
    if url not in user_access[user_id]:
        return {"error": 'Invalid access'}

    payload={
            'url':url,
            'perms':perms,
            'user_id':user_id
        }
    token=jwt.encode(payload,jwt_key,algorithm='HS256')
    return token

@app.route('/check_access',methods=['GET'])
def check_access():
        token = request.args.get('access_token')
        root.info('started')
        payload=jwt.decode(token,jwt_key)
        root.info('decoding:status completd')
        return payload



if __name__ == '__main__':
    app.run(port='5004',debug=True)

