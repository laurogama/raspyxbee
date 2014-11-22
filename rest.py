from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

endpoints = [{'name': 'tomada1',
              'actions': [{'command': 'ligar', 'description': 'turns the power outlet ON',
                           'example': '/api/endpoints/tomada1/ligar', },
                          {'command': 'desligar', 'description': 'turns the power outlet OFF'}]},
             {'name': 'tomada2', 'actions': []}]


@app.route("/")
def hello():
    return "Snakebed! A REST API for iteracting with IOT devices using Flask."


def execute_action(id, action):
    return "execute action: " + action + " on device: " + id


class Endpoints(restful.Resource):
    def get(self, id=None, action=None):
        if id is not None:
            for endpoint in endpoints:
                if endpoint.get('name') == id:
                    if action is not None:
                        for act in endpoint.get('actions'):
                            if act.get('command') == action:
                                return execute_action(id, action)
                    return endpoint
        return endpoints


api.add_resource(Endpoints, '/api/endpoints', '/api/endpoints/<string:id>',
                 '/api/endpoints/<string:id>/<string:action>',
                 endpoint='get')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
