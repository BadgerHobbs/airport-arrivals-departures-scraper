from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from scrapers.heathrow import Heathrow

app = Flask(__name__)
CORS(app)
app.debug = True

airports = [
    Heathrow()
]

@app.route('/api/v1/airports', methods=['GET'])
def get_airports():
    return jsonify({
        'airports': [
        ]
    })

@app.route('/api/v1/arrivals', methods=['GET'])
def get_arrivals():

    # Get the airport/code from the URL
    airport_code = request.args.get('airport_code')
    airport = request.args.get('airport')

    # If no airport code is provided, return an error
    if not airport_code and not airport:
        return jsonify({
            'error': 'No airport provided'
        }), 400

    # Get airport by code or name
    airport = next((a for a in airports if a.code == airport_code or a.full_name == airport), None)

    # If no airport is found, return an error
    if not airport:
        return jsonify({
            'error': f'No airport found with code or name: {airport_code or airport}'
        }), 400

    # Get arrivals for the airport
    return jsonify({
        'arrivals': airport.arrivals()
    })

@app.route('/api/v1/departures', methods=['GET'])
def get_departures():

    # Get the airport/code from the URL
    airport_code = request.args.get('airport_code')
    airport = request.args.get('airport')

    # If no airport code is provided, return an error
    if not airport_code and not airport:
        return jsonify({
            'error': 'No airport provided'
        }), 400

    # Get airport by code or name
    airport = next((a for a in airports if a.code == airport_code or a.full_name == airport), None)

    # If no airport is found, return an error
    if not airport:
        return jsonify({
            'error': f'No airport found with code or name: {airport_code or airport}'
        }), 400

    # Get departures for the airport
    return jsonify({
        'departures': airport.departures()
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)