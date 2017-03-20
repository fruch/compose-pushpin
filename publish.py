import time

import consul
from gripcontrol import GripPubControl

from pubcontrol import PubControl, PubControlClient, Item, Format

class HttpResponseFormat(Format):
    def __init__(self, body):
        self.body = body
    def name(self):
        return 'http-response'
    def export(self):
        return {'body': self.body}


def callback(result, message):
    if result:
        print('Publish successful')
    else:
        print('Publish failed with message: ' + message)

controls = []

c = consul.Consul()
'''
i, services = c.catalog.service('pushpin-5561')
for service in services:
    print service['ServiceAddress'], service['ServicePort']
    controls += [{'control_uri': 'http://{ServiceAddress}:{ServicePort}'.format(**service)}]

pub = GripPubControl(controls)

for i in range(100):
    print ("sending")
    time.sleep(10)
    pub.publish_http_response('mychannel', '{"hello": "world"}\n', blocking=False, callback=callback)
'''

zmq_controls = []
i, services = c.catalog.service('pushpin-5562')
for service in services:
    print service['ServiceAddress'], service['ServicePort']
    zmq_controls += [{'zmq_pub_uri': 'tcp://{ServiceAddress}:{ServicePort}'.format(**service), 'require_subscribers': True}]


print zmq_controls
pub = PubControl(zmq_controls)

for i in range(100):
    print ("sending")
    time.sleep(10)
    pub.publish('mychannel', Item(HttpResponseFormat('{"hello": "world"}\n')), blocking=False, callback=callback)

