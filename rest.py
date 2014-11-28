from flask import Flask, render_template
from flask.ext import restful
from flask.ext.bootstrap import Bootstrap

from commandHandler import EndpointHandler


app = Flask(__name__)
api = restful.Api(app)
Bootstrap(app)
endpoints = [
    {
        'name': 'tomada1',
        'xbee_id': '40ABBC08',
        'actions': [{'command': 'ligar', 'description': 'turns the power outlet ON',
                     'example': '/api/endpoints/tomada1/ligar', },
                    {'command': 'desligar', 'description': 'turns the power outlet OFF'}]
    },
    {
        'name': 'tomada2',
        'xbee_id': '40ABBA21',
        'actions': [
            {'command': 'ligar', 'description': 'turns the power outlet ON',
             'example': '/api/endpoints/tomada2/ligar', },
            {'command': 'desligar', 'description': 'turns the power outlet OFF'}
        ]
    },
    {
        'name': 'tomada3',
        'xbee_id': '40ABB938',
        'actions': [
            {'command': 'ligar', 'description': 'turns the power outlet ON',
             'example': '/api/endpoints/tomada3/ligar', },
            {'command': 'desligar', 'description': 'turns the power outlet OFF'}
        ]
    },
    {
        'name': 'infrared1',
        'xbee_id': '40ABBA0B',
        'actions': [
            {'command': 'power', 'description': 'turns the power ON or OFF',
             'example': '/api/endpoints/infrared1/power', },
            {'command': 'canalup', 'description': 'increases the channel',
             'example': '/api/endpoints/infrared1/canalup', },
            {'command': 'canaldown', 'description': 'decreases the channel',
             'example': '/api/endpoints/infrared1/canaldown', },
            {'command': 'volumeup', 'description': 'turns the volume UP',
             'example': '/api/endpoints/infrared1/volumeup', },
            {'command': 'volumedown', 'description': 'turns the volume DOWN',
             'example': '/api/endpoints/infrared1/volumedown', },
        ]
    }
]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

@app.route("/tests")
def tests():
    return render_template("tests.html")

class Endpoint(restful.Resource):
    def get(self, id=None, action=None):
        if id is not None:
            for endpoint in endpoints:
                if endpoint.get('name') == id:
                    if action is not None:
                        for act in endpoint.get('actions'):
                            if act.get('command') == action:
                                # print endpoint['xbee_id']
                                return EndpointHandler.send_message(endpoint['xbee_id'], action)
                    return endpoint
        return endpoints


class Router(restful.Resource):
    def get(self):
        return {'xbee_id': '40ABBB4E'}


api.add_resource(Endpoint,
                 '/api/endpoint/',
                 '/api/endpoint/<string:id>',
                 '/api/endpoint/<string:id>/<string:action>',
)

api.add_resource(Router, '/api/router')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
