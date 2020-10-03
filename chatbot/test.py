from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["오늘의 뉴스보기"]
    }

    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def message():

    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == u"시작하기":
        dataSend ={
            "message" : {
                "text" : "시작하기 테스트입니다."
            }
        }

    elif content == u"안녕하세요":
        dataSend ={
            "message" : {
                "text" : "반갑습니다 어서오세요."
            }
        }

    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5050, debug=True)
