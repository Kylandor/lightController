from flask import Flask, render_template, url_for, jsonify, request
import math
import createData

app = Flask(__name__)
@app.route("/", methods = ['POST'] )
def home():
    f = open('frames', 'ab')
    frame = []
    numberOfSec = 0
    data = request.data
    data = data.decode("utf-8")
    numberOfSec = float(data[data.index("sec=")+4:])
    data = data.split("rgb")
    data = data[1:]
    for i in data:
        cur = i[1:i.index(")")]
        cur = cur.split(", ")
        frame.append((int(cur[0]), int(cur[1]), int(cur[2])))
    print(numberOfSec)
    frameData = createData.makePacket(frame)
    frameData = frameData * math.ceil(25 *numberOfSec)
    frameData.tofile(f)
    f.close()
    return "ok"
@app.route("/clear", methods = ['GET'] )
def clearFrame():
    open("frames", 'w').close()
    return "cleared"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '192.168.1.38')