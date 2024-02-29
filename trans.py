from flask import Flask, jsonify

app = Flask(__name__)

variable_value = "Hello from Python"

@app.route('/api/get-variable', methods=['GET'])
def get_variable():
    return jsonify({'variable': variable_value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)