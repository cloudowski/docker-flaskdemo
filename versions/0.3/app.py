from flask import Flask, abort
from flask import request
from flask import jsonify
import socket
import datetime

version = '0.3'
hitCount = 0
startDT = datetime.datetime.now()
startTime = startDT.strftime("%Y-%b-%d %H:%M:%S")

app = Flask(__name__)

@app.route("/")
def show_details() :
    global startTime
    global hitCount
    global version
    hitCount = hitCount + 1
    return "<html>" + \
           "<head><title>Docker + Flask Demo</title></head>" + \
           "<body>" + \
           "<table>" + \
           "<tr><td> Start Time </td> <td>" +  startTime + "</td> </tr>" \
           "<tr><td> Hostname </td> <td>" + socket.gethostname() + "</td> </tr>" \
           "<tr><td> Local Address </td> <td>" + socket.gethostbyname(socket.gethostname()) + "</td> </tr>" \
           "<tr><td> Remote Address </td> <td>" + request.remote_addr + "</td> </tr>" \
           "<tr><td> Server Hit </td> <td>" + str(hitCount) + "</td> </tr>" \
           "<tr style='color:green'><td> App Version</td> <td>" + str(version) + "</td> </tr>" \
           "</table>" + \
           "</body>" + \
           "</html>"

@app.route("/version")
def print_version() :
    global version
    return str(version)

@app.route("/json")
def send_json() :
    global startTime
    global hitCount
    global version
    hitCount = hitCount + 1
    return jsonify( {'StartTime' : startTime,
                     'Hostname': socket.gethostname(),
                     'LocalAddress': socket.gethostbyname(socket.gethostname()),
                     'RemoteAddress':  request.remote_addr,
                     'Server Hit': str(hitCount),
                     'Version':  str(version)} )

@app.route("/healthz")
def healthz():
    delta = datetime.datetime.now()-startDT
    if delta.seconds > 300:
        abort(451)
    return 'OK'

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 8080)
