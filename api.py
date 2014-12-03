# coding=utf-8
import time
from flask import jsonify

from commandHandler import EndpointHandler
from commandHandler.cameraHandler import take_picture


__author__ = 'laurogama'
from flask.ext import restful

endpoints = [
    # {
    # 'name': 'tomada1',
    #     'xbee_id': '40ABBC08',
    #     'actions': [
    #         {'command': 'ligar', 'description': 'turns the power outlet ON',
    #          'example': '/api/endpoint/tomada1/ligar', },
    #         {'command': 'desligar', 'description': 'turns the power outlet OFF'},
    #         {'command': 'estado', 'description': 'queries the actual status of the device'}
    #     ]
    # },
    {
        'name': 'alimentator',
        'xbee_id': '40ABBC08',
        'actions': [
            {'command': 'food', 'description': 'libera comida'},
            {'command': 'water', 'description': 'libera agua'}
        ]
    },
    {
        'name': 'sharp',
        'xbee_id': '40ABBA21',
        'actions': [
            {'command': 'distancia'}
        ]
    },
    # {
    #     'name': 'tomada3',
    #     'xbee_id': '40ABB938',
    #     'actions': [
    #         {'command': 'ligar', 'description': 'turns the power outlet ON',
    #          'example': '/api/endpoint/tomada3/ligar', },
    #         {'command': 'desligar', 'description': 'turns the power outlet OFF'},
    #         {'command': 'estado', 'description': 'queries the actual status of the device'}
    #     ]
    # },
    {
        'name': 'cesto',
        'xbee_id': '40ABB938',
        'actions': [
            {'command': 'desligar', 'description': 'desliga todos os leds'},
            {'command': 'vermelho', 'description': 'queries the actual status of the device'},
            {'command': 'verde', 'description': 'queries the actual status of the device'},
            {'command': 'laranja', 'description': 'queries the actual status of the device'}

        ]
    },
    {
        'name': 'porta',
        'xbee_id': '40ABB8A2',
        'actions': [
            {'command': 'desligar', 'description': 'fecha a porta'},
            {'command': 'ligar', 'description': 'abre a porta'},
            {'command': 'estado', 'description': 'queries the actual status of the device'}
        ]
    },
    {
        'name': 'medidor',
        'xbee_id': '40ABB6E9',
        'actions': [
            {'command': 'energia', 'description': 'queries the actual status of the device'}
        ]
    },
    {
        'name': 'infrared1',
        'xbee_id': '40ABBA0B',
        'actions': [
            {'command': 'power', 'description': 'turns the power ON or OFF',
             'example': '/api/endpoint/infrared1/power', },
            {'command': 'canalup', 'description': 'increases the channel',
             'example': '/api/endpoint/infrared1/canalup', },
            {'command': 'canaldown', 'description': 'decreases the channel',
             'example': '/api/endpoint/infrared1/canaldown', },
            {'command': 'volumeup', 'description': 'turns the volume UP',
             'example': '/api/endpoint/infrared1/volumeup', },
            {'command': 'volumedown', 'description': 'turns the volume DOWN',
             'example': '/api/endpoint/infrared1/volumedown', },
            {'command': 'estado', 'description': 'queries the actual status of the device'}
        ]
    }
]
router = {'xbee_id': '40ABBB4E'}


class APIEndpoint(restful.Resource):
    def get(self, id=None, action=None):

        if id is not None:
            for endpoint in endpoints:
                if endpoint.get('name') == id:
                    if action is not None:
                        for act in endpoint.get('actions'):
                            if act.get('command') == action:
                                return jsonify(EndpointHandler.send_message(endpoint['xbee_id'], action))
                    return endpoint
        return endpoints


class APIRouter(restful.Resource):
    def get(self):
        return router


class APICamera(restful.Resource):
    def get(self, action=None):
        print action
        if 'takepicture' == action:
            take_picture()
            time.sleep(1)
        return