#!/usr/bin/env python
import os
import json
import random
from httplib import HTTPException
from urllib2 import HTTPError, URLError

from flask import Flask, jsonify, make_response, request

APP = Flask(__name__)
LOG = APP.logger


@APP.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    print("Request:")
    print(json.dumps(req))
    jobName=req["queryResult"]["parameters"]["jobName"]
    os.system('curl -k -X POST https://sebuild.tejdrive.com:12443/job/'+jobName+'/build --user zzzzzzzzzzz:xxxxxxxxxx')
    #os.system('curl -k -X POST https://sebuild.tejdrive.com:12443/job/Test-Rohit/build --user rxxxxxxxx:xxxxxxxxxxx')
    return jsonify(req)

webhookinput = (webhook)

print webhookinput

if __name__ == '__main__':
    PORT = 8080

    APP.run(
        debug=True,
        port=PORT,
        host='0.0.0.0'
    )
