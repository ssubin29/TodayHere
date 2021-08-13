#import flask
from flask import Flask, request, jsonify

app = Flask(__name__)

#서버가 정상적으로 작동되는지 확인
#https://url.com
@app.route("/")
def hello():
    return "Hello, Flask!"

#https://url.com/coffe
@app.route('/coffe', methods=['POST'])
def coffe():
    req = request.get_json()

    coffe_menu = req["action"]["datailParams"]["coffe_menu"]["value"]

    answer = coffe_menu
    #answer = "아메리카노"

        #답변 설정
    res = {
        "version":"2.0",
        "template":{
            "outputs": [
                {
                    "simpleText":{
                        "text":answer
                    }
                }
            ]
        }
    }
        #답변 발사!
    return jsonify(res)

#메인 함수
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)