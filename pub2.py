# this program uses pushpin's SUB socket to publish

import sys
import time
import tnetstring
import zmq
import consul

if len(sys.argv) < 3:
    print('usage: %s [channel] [content]' % sys.argv[0])
    sys.exit(1)

channel = sys.argv[1]
content = sys.argv[2]

c = consul.Consul()

ctx = zmq.Context()

# note: in a typical long-running program you'd use a normal PUB socket and
# send messages when needed:
#
#   sock = ctx.socket(zmq.PUB)
#   sock.connect(...)
#   ...
#   sock.send_multipart([channel, {item}])
#
# however, since this is a short-running program, we'll use XPUB and wait a
# moment for the subscription to arrive. this is bad practice, though. if you
# need to publish from a short-running program in real life, use pushpin's
# PULL socket, or create a long-running broker that uses PUB to pushpin and
# a PULL socket for input.

sock = ctx.socket(zmq.PUB)
i, services = c.catalog.service('push_pushpin-5562')
for service in services:
    print service['ServiceAddress'], service['ServicePort']
    sock.connect('tcp://{ServiceAddress}:{ServicePort}'.format(**service))

poller = zmq.Poller()
poller.register(sock, zmq.POLLIN)
start = int(time.time() * 1000)
while True:
    elapsed = int(time.time() * 1000) - start
    if elapsed >= 500:
        # give up
        print("giveup")
        break
    socks = dict(poller.poll(500 - elapsed))
    if socks.get(sock) == zmq.POLLIN:
        m = sock.recv()
        print m
        if m[0] == '\x01' and m[1:] == channel:
            # subscription ready
            break

hr = dict()
hr['body'] = content + '\n'
hs = dict()
hs['content'] = content + '\n'
ws = dict()
ws['content'] = content
formats = dict()
formats['http-response'] = hr
formats['http-stream'] = hs
formats['ws-message'] = ws
item = dict()
item['formats'] = formats

print(item)
print( tnetstring.dumps(item))
sock.send_multipart([channel, tnetstring.dumps(item)])

print('Published')
