import os
import webbrowser
from threading import Timer

from flask import Flask, render_template

KATSU_ENV = os.environ.get('KATSU_ENV')

DEBUG = False if KATSU_ENV is not None else True
PORT = os.environ.get('KATSU_PORT', '5000')
APP_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(APP_DIR,
                             'web/build/static') if not DEBUG else 'static'
TEMPLATE_FOLDER = os.path.join(APP_DIR,
                               'web/build') if not DEBUG else 'templates'

app = Flask(
    __name__,
    static_folder=STATIC_FOLDER,
    template_folder=TEMPLATE_FOLDER,
)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if DEBUG:
        return 'PyBaQ - api'
    return render_template('index.html')


@app.route('/api/participants/')
def participants():
    return 'TBD '


@app.route('/api/rewards/')
def rewards():
    return 'TBD'


def open_browser():
    if not DEBUG:
        webbrowser.open_new(f'http://127.0.0.1:{PORT}/')


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=DEBUG, port=PORT)
