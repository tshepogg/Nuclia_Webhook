import requests
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Retrieve API key and Knowledge Box ID from environment variables
API_KEY = os.getenv('NUCLIA_API_KEY')
KB_ID = os.getenv('NUCLIA_KB_ID')

if not API_KEY or not KB_ID:
    raise ValueError("Please set the NUCLIA_API_KEY and NUCLIA_KB_ID environment variables.")

# Base URL for your Knowledge Box
BASE_URL = f'https://{KB_ID}.nuclia.cloud/api/v1'

# Headers for authentication
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def search_knowledge_box(query):
    """
    Perform a search query in the Knowledge Box.
    """
    url = f'{BASE_URL}/search'
    payload = {
        'query': query
    }
    response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return None

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400
    results = search_knowledge_box(query)
    if results:
        return jsonify(results), 200
    else:
        return jsonify({'error': 'Failed to retrieve results'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
