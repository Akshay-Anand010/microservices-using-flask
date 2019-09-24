from flask import Flask
from logger import root
from flask import request
app = Flask(__name__)
count={}
import time
import requests
import jwt

@app.route("/count",methods=['GET'])
def counter():
    global count;

    url=request.args.get('url')
    root.info('calculating count in url occours {} status processing'.format(url))
    if not url in count:
        count[url]=1
    else:
        count[url]+=1
        root.info('calculating count in url  {}'
                   'status successful'
                    'result:{}'.format(url,count))
        return str(count[url])




if __name__ == '__main__':
    app.run(port='5002',debug=True)