from flask import Flask, render_template, Response
import cv2 as cv
app = Flask(__name__)
camera = cv.VideoCapture(0)

def gen_frames(time=0):
    while True:
        success,frame = camera.read()
        if not success:
            break
        else:
            ret,buffer = cv.imencode('.jpg',frame)
            frame = buffer.tobytes()
            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
# 允许所有ip访问
# 如果设置debug=True，而忽略use_reloader，则Ubuntu1604浏览器无法正确显示视频流
# 可以通过设置debug=False或者设置use_reloader=False解决
# Win10没有这个问题
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,use_reloader= False)