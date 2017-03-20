from bottle import route, run, template, response, request

@route('/hello/<name>')
def index(name):
    response.set_header('Grip-Hold', 'response')
    response.set_header('Grip-Channel', 'mychannel')
    response.set_header('Grip-Timeout', '15')
    response.set_header('Grip-Keep-Alive', '.; format=cstring; timeout=1')

    print(dict(request.headers))
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='0.0.0.0', port=8080, debug=True)
