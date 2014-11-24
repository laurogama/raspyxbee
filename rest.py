from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

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
        'xbee_id': '40ABBB4E',
        'actions': [
            {'command': 'ligar', 'description': 'turns the power outlet ON',
             'example': '/api/endpoints/tomada3/ligar', },
            {'command': 'desligar', 'description': 'turns the power outlet OFF'}
        ]
    },
    {
        'name': 'infrared1',
        'xbee_id': '40ABB842',
        'actions': [
        ]
    },
    {
        'name': 'infrared2',
        'xbee_id': '40ABBA0B',
        'actions': [
        ]
    }
]


@app.route("/")
def hello():
    return "Snakebed! A REST API for iteracting with IOT devices using Flask."


def execute_action(endpoint, action):
    # TODO implement backend calls
    return "execute action: " + action + " on device: " + endpoint['name']


class Endpoint(restful.Resource):
    def get(self, id=None, action=None):
        if id is not None:
            for endpoint in endpoints:
                if endpoint.get('name') == id:
                    if action is not None:
                        for act in endpoint.get('actions'):
                            if act.get('command') == action:
                                return execute_action(endpoint, action)
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
