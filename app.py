from flask import Flask, jsonify, render_template
from flask_cors import CORS
from zadarma.zadarma import ZadarmaAPI

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)
zadarma = ZadarmaAPI()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/saldo')
def saldo():
    return jsonify(zadarma.get_balance())

@app.route('/api/llamadas')
def llamadas():
    return jsonify(zadarma.get_call_history())

@app.route('/api/grabaciones')
def grabaciones():
    return jsonify(zadarma.get_recordings())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
