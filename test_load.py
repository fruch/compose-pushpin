from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

import consul

agent = Agent(reactor)


c = consul.Consul()
urls = []

i, services = c.catalog.service('pushpin-7999')
for service in services:
    print service['ServiceAddress'], service['ServicePort']
    urls += ['http://{ServiceAddress}:{ServicePort}/hello/test'.format(**service)]

print urls

num = 0
for i in range(10000):
    d = agent.request(
        'GET',
    urls[i%3],
    None,
    None)

    def cbResponse(response):
        global num
        num = num + 1
        print num 
        if response.code != 200:
            print 'Response code:', response.code
    def error(err):
        global num
        num = num + 1
        print num  
        print err
    d.addCallback(cbResponse)
    d.addErrback(error)
reactor.run()
