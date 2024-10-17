# Python 3 server example
# https://pythonbasics.org/webserver/
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from showCourses import ShowStr

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        file=open("indexTop.html","r")
        top=file.read()
        self.wfile.write(bytes(top, "utf-8"))
        file.close()

        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        # get the current class list?
        self.wfile.write(bytes(ShowStr(), "utf-8"))

        file=open("indexBottom.html","r")
        bottom=file.read()
        self.wfile.write(bytes(bottom, "utf-8"))
        file.close()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")