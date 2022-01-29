# -*-Coding=utf-8-*-


from flask import Flask

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def error_api_status():
    a = '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    print('test ---------------')
    return 'error api_status'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10421, debug=True)

