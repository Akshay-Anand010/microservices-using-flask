from flask import Flask
from flask import request
from logger import root
app = Flask(__name__)

import time
import requests
import jwt

@app.route("/timer",methods=['GET'])
def timer():
        start_time = time.time()*1000
        url=request.args.get('url')
        root.info('calculating time in url occours {} status processing'.format(url))
        requests.get(url)
        end_time = time.time()*1000
        root.info('calculating count in url  {}'
                  'status successful'
                  'result:{}'.format(url, time))
        return time


if __name__ == '__main__':
    app.run(port='5003',debug=True)