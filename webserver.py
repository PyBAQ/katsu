import os
import csv
import uuid
import webbrowser
from threading import Timer

from flask import Flask, render_template, request
from collections import namedtuple

from flask_cors import CORS

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

CORS(app)


def serializer(data, many=False):
    if many:
        data_dict = [dict(d._asdict()) for d in data]
    else:
        data_dict = dict(data._asdict())
    return data_dict


def get_value(row):
    data = row.split(',')
    data.append(uuid.uuid4())
    return data


def cvsReader(filename, name):
    reader = iter(filename.read().decode('utf-8').split())
    subclass = namedtuple(name, next(reader))
    subclass = namedtuple(name, subclass._fields + ('id', ))
    return [subclass(*get_value(row)) for row in reader]


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


@app.route('/api/upload/', methods=['POST'])
def upload():

    if len(request.files) != 2:
        print('if 1')
        return '', 400

    if 'participants' not in request.files.keys():
        return '', 400

    if 'rewards' not in request.files.keys():
        return '', 400

    participants = request.files['participants']
    rewards = request.files['rewards']

    participants = cvsReader(participants, 'participants')
    rewards = cvsReader(rewards, 'rewards')
    return {
        'data': {
            'participants': serializer(participants, many=True),
            'rewards': serializer(rewards, many=True)
        }
    }, 200


def open_browser():
    if not DEBUG:
        webbrowser.open_new(f'http://127.0.0.1:{PORT}/')


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=DEBUG, port=PORT)
