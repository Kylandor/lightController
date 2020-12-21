from flask import Flask, render_template, url_for, jsonify, request
import createData

app = Flask(__name__)
@app.route("/", methods = ['POST'] )
def home():
    f = open('frames', 'ab')
    frame = []
    data = request.data
    data = data.decode("utf-8")
    data = data.split("rgb")
    data = data[1:]
    for i in data:
        cur = i[1:i.index(")")]
        cur = cur.split(", ")
        frame.append((int(cur[0]), int(cur[1]), int(cur[2])))
    frameData = createData.makePacket(frame)
    frameData.tofile(f)
    f.close()
    return "ok"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '192.168.1.38')