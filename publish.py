# from gripcontrol import GripPubControl

from pubcontrol import PubControl, PubControlClient, Item, Format

class HttpResponseFormat(Format):
    def __init__(self, body):
        self.body = body
    def name(self):
        return 'http-response'
    def export(self):
        return {'body': self.body}

import time

def callback(result, message):
    if result:
        print('Publish successful')
    else:
        print('Publish failed with message: ' + message)


pub = PubControl(
       {'zmq_uri': 'tcp://pushpin:5563',
        'require_subscribers': False}
)
#{
#    'control_uri': 'http://pushpin:5561'
#})

#pub.apply_grip_config({'control_zmq_uri': 'tcp://pushpin:5563',
#        'require_subscribers': True})

for i in range(100):
    time.sleep(10)
    pub.publish('mychannel', Item(HttpResponseFormat('{"hello": "world"}\n')), blocking=True, callback=callback)

