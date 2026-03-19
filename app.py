from flask import Flask, request, jsonify

app = Flask(__name__)

last_signal = ""

@app.route('/webhook', methods=['POST'])
def webhook():
    global last_signal
    data = request.json
    
    try:
        last_signal = data['message']['text']
        print("Sinal recebido:", last_signal)
    except:
        pass

    return "ok"

@app.route('/signal', methods=['GET'])
def get_signal():
    return jsonify({"signal": last_signal})

app.run(host='0.0.0.0', port=10000)
