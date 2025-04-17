from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/new-mail', methods=['POST'])
def api_endpoint():
    print("Received a POST request")
    data = request.get_json()
    if not data:
        print(jsonify({"error": "No JSON data provided"}))
    print(jsonify({"message": "Data received", "data": data}))

@app.route('/new-mail', methods=['GET'])
def api_endpoint_get():
    print("Received a GET request")
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)