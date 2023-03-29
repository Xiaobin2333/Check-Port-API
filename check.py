import os
import sys
import flask
from tcping import Ping


app = flask.Flask(__name__)


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


def tcping(server, port):
    ping = Ping(server, port, 1)
    try:
        with HiddenPrints():
            ping.ping(4)
    except Exception as e:
        return None
    rate = Ping._success_rate(ping)
    if float(rate) > 0:
        return True
    return False


@app.route('/check', methods=['GET'])
def check():
    server = flask.request.args.get('server')
    port = flask.request.args.get('port')
    if server is None or port is None:
        return "server or port is None", 400
    result = tcping(server, port)
    if result is None:
        return "Error", 500
    elif result:
        return "True", 200
    else:
        return 'False', 200


app.run(host='0.0.0.0', port=5000)
