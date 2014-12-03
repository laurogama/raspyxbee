import time

from flask import Flask, render_template, make_response

from flask.ext import restful
from flask.ext.bootstrap import Bootstrap
from flask.ext.cors import CORS

from api import endpoints, router, APIEndpoint, APIRouter, APICamera

from commandHandler import EndpointHandler

from commandHandler.cameraHandler import take_picture
from settings import headers


app = Flask(__name__)
cors = CORS(app)
api = restful.Api(app)
Bootstrap(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/documentation")
def documentation():
    return make_response(render_template("documentation.html", endpoints=endpoints, router=router), 200, headers)


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
                                return make_response(render_template("result.html", endpoint=None,
                                                                     action=EndpointHandler.send_message(
                                                                         endpoint['xbee_id'], action)), 200,
                                                     headers)
                    return make_response(render_template("result.html", endpoint=endpoint), 200,
                                         headers)
        return endpoints


class Router(restful.Resource):
    def get(self):
        return make_response(render_template("result.html", router=router), 200,
                             headers)


class Camera(restful.Resource):
    def get(self, action=None):
        print action
        if 'takepicture' == action:
            take_picture()
            time.sleep(1)
        return make_response(render_template("picture.html"))


api.add_resource(Endpoint,
                 '/endpoint/',
                 '/endpoint/<string:id>',
                 '/endpoint/<string:id>/<string:action>',
)

api.add_resource(Router, '/router')

api.add_resource(Camera, '/camera/', '/camera/<string:action>')

api.add_resource(APIEndpoint,
                 '/api/endpoint/',
                 '/api/endpoint/<string:id>',
                 '/api/endpoint/<string:id>/<string:action>',
)

api.add_resource(APIRouter, '/api/router')

api.add_resource(APICamera, '/api/camera/', '/api/camera/<string:action>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)