# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import json
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv('NUCLIA_API_KEY')
KB_ID = os.getenv('NUCLIA_KB_ID')
BASE_URL = f'https://europe-1.nuclia.cloud/api/v1/kb/{KB_ID}'

HEADERS = {
    'X-NUCLIA-SERVICEACCOUNT': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def search_knowledge_box(query):
    url = f'{BASE_URL}/search'
    payload = {'query': query}
    response = requests.post(url, headers=HEADERS, data=json.dumps(payload), verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': response.status_code, 'message': response.text}

@app.route('/api/search', methods=['POST'])
def api_search():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({'error': 'Query not provided'}), 400
    result = search_knowledge_box(query)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
