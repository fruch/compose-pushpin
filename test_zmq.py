import zmq
import random
import sys
import time

port = "5562"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://127.0.0.1:%s" % port)

port = "5560"
p_socket = context.socket(zmq.PUSH)
p_socket.connect("tcp://127.0.0.1:%s" % port)



while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215) - 80
    print("%d %d" % (topic, messagedata))
    socket.send_string("%d %d" % (topic, messagedata))
    p_socket.send_string("%d %d" % (topic, messagedata))
    time.sleep(1)
