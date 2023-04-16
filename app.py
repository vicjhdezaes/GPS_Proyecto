from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/sumar')
def sumar():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({'resultado': a + b})

@app.route('/restar')
def restar():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({'resultado': a - b})

@app.route('/multiplicar')
def multiplicar():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({'resultado': a * b})

@app.route('/dividir')
def dividir():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({'resultado': a / b})

if __name__ == '__main__':
    app.run()
