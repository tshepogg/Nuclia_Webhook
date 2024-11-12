# app.py
from flask import Flask, request, jsonify, render_template
import requests
import json
import os
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

# Environment variables for API_KEY and KB_ID
API_KEY = 'eyJhbGciOiJSUzI1NiIsImtpZCI6InNhIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2V1cm9wZS0xLm51Y2xpYS5jbG91ZC8iLCJpYXQiOjE3MzE0MDcyNzAsInN1YiI6IjdiOTZkZDlkLTA5NjktNDAxNC1hN2IxLTBkYjBkZmZjYTI2YiIsImp0aSI6IjhkZDRlNDg4LTcxNjUtNDk1OC1hZWFmLTNjOGFjZmQ4ZWY2YiIsImV4cCI6MTc2Mjk0MzI3MCwia2V5IjoiYTMxZGZjYTUtYTgzMy00MmQxLTg5NmQtYTAwMWQyNzJiNmNiIiwia2lkIjoiMjc1MjgyYzUtOGNkOS00NjRmLWE2MzktYWViYjI2ZDFjNjhlIn0.hhov_IJBpO-9aX0smlwbEwJzEjTsN-4biqEFw9X4HeCo9ihg_TNNDQc3mOF7dNg5P5qhCHgJYeNASPWbc8Fq62SFMmU5ckgn3_PRubSZ_pt6Rzdyh523IhkOX1a9Fp1mB2vYzqQRdnLrLo6XHEF5vgggUrulZi1W3IVSNZ7uklCwQPyLW_L7kS55wzUVogVoE61uqpriRDNM1wJSLO9p-0B2cxh6Z_i45WmQmePvG2Ucv2SsWcHS_pvFGmi9nCK2O5CUQ07NRvMmAELrQgcWA_WotjCQ2W2tkerOGJC2FlnkBxMiXIbExy-AI4iSPQ_OjeHIpB2IS9YxuCLzYWHY4sndD0WbDz6cZbPRwps64Y9OGdRUWDxnGIvdEURdQbQ89p_QQj_s3DtwdreY3VTw4WGBPoEusw-yjZLOqlgAcFqaPlKeocD0BOHKDAIebuwKKXkmEwD0PLg_kEmbrUYpGtwtIarjPxs7fkAIwSQ5PyDzpfBKAqRpPt7s7AmwHwC828dXL5sz6hrV9aMvR3N576YYOFeTdzWWIxeqGR8QQz6keDQcuvcFWy09q7VgTYgZOZ4pSdVcfaHBivVITF_OmuVYAUtjtxcJYaHU2K3n99OkSnQmfBpBY_Cj8T4p87Wqga0_oS8MTJIQZu0RUEZKagsmFmjHrCt4ztzC7pfzel8'
KB_ID = '903a0322-3d77-4ec3-94fd-3a10021c9500'
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

@app.route('/')
def home():
    return render_template('index.html')

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
