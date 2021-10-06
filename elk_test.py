import json
import logging
import random
import time
import traceback

from flask import Flask, request

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def test():
    print('elk test------------------------------------------')
    #data = request.get_json()
    #print(data)
    return "elk response"


@app.route('/', methods=['GET', 'POST'])
def root():
    data = request.get_json()
    print(data)
    return 'hello word'
    action = request.args.get('action', '')
    data = request.get_json()
    data['request_id'] = int(time.time() * 1000)
    data['action'] = action
    data['url'] = "http://test.test.test/{}".format(random.randint(1000, 3000000))
    data['action'] = action
    data['ip_addr'] = request.remote_addr
    if action == 'info':
        app.logger.info(data)
    elif action == 'warning':
        app.logger.warning(data)
    elif action == 'error':
        try:
            a = b
        except Exception as e:
            data_error = {
                'request_id': int(time.time() * 1000),
                'ip_addr': request.remote_addr,
                'action': action,
                'url': "http://test.test.test/{}".format(random.randint(1000, 3000000)),
                'msg': 'error ' + str(e),
                # "elast_alert_type": "any"
            }
            # app.logger.info(data_error)
            # app.logger.info(traceback.print_exc())
            app.logger.info(traceback.format_exc())
            print(traceback.format_exc())

    else:
        app.logger.warning(data)
    return json.dumps(data)


if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('/home/glfadd/Desktop/logs/flask.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run()
