var http = require("http");
var server = http.createServer(function(request, response) {
  response.writeHead(200, { "Grip-Hold": "response", 
                            "Grip-Channel": "mychannel", 
                            "Grip-Timeout": "60"});
  response.write('<b>Hello {{name}}</b>!');
  response.end();
});

server.listen(8080);
console.log("Server is listening");
