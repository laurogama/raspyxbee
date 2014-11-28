__author__ = 'laurogama'


class ModelEndpoint():
    def get(self):
        return [
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