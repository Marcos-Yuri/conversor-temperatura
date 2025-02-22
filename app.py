from flask import Flask, request, jsonify
from conversor import celsius_para_fahrenheit, fahrenheit_para_celsius

app = Flask(__name__)

@app.route('/celsius-para-fahrenheit', methods=['GET'])
def celsius_para_fahrenheit_api():
    try:
        celsius = float(request.args.get('celsius'))
        fahrenheit = celsius_para_fahrenheit(celsius)
        return jsonify({'celsius': celsius, 'fahrenheit': fahrenheit}), 200
    except (ValueError, TypeError):
        return jsonify({'error': 'Valor inválido para celsius'}), 400

@app.route('/fahrenheit-para-celsius', methods=['GET'])
def fahrenheit_para_celsius_api():
    try:
        fahrenheit = float(request.args.get('fahrenheit'))
        celsius = fahrenheit_para_celsius(fahrenheit)
        return jsonify({'fahrenheit': fahrenheit, 'celsius': celsius}), 200
    except (ValueError, TypeError):
        return jsonify({'error': 'Valor inválido para fahrenheit'}), 400

if __name__ == '__main__':
    app.run(debug=True)
