# Python 3 server example
# https://pythonbasics.org/webserver/

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from showCourses import ShowStr
from addCourses import addCourse
from delCourses import deleteCourse

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def sendFile(self,filename,mimetype):
        self.send_response(200)
        self.send_header("Content-type",mimetype)
        self.end_headers()
        file=open(filename,"r")
        top=file.read()
        self.wfile.write(bytes(top, "utf-8"))
        file.close()
    def sendHTMLHeader(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        print("Do Get")
        if (self.path.startswith("/index.html") or self.path=="/"):
            self.sendFile("index.html","text/html")
        elif (self.path.startswith("/code.js")):
            self.sendFile("code.js","text/javascript")
        elif (self.path.startswith("/styles.css")):
            self.sendFile("styles.css","text/css")
        elif (self.path.startswith("/courses")):
            self.sendHTMLHeader()
            self.wfile.write(bytes(ShowStr(False),"utf-8"))
        else:
            urlParts=self.path.split('?')
            if len(urlParts)>1:
                nameValues=urlParts[1].split('&')
                d = dict(x.split("=") for x in urlParts[1].split("&"))
                if (self.path.startswith("/add")):
                    self.sendHTMLHeader()
                    addCourse(d['class'],d['number'])
                elif (self.path.startswith("/del")):
                    self.sendHTMLHeader()
                    deleteCourse(d['class'],d['number'])

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")