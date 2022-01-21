# -*-coding=utf-8-*-
import pdb; pdb.set_trace()

import datetime
import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def error_api_status():
    print(123)
    print('test ---------------')
    return 'error api_status'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True, processes=1,threaded=True)

