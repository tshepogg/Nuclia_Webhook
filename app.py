import requests
import json
import os

# Retrieve API key and Knowledge Box ID from environment variables
API_KEY = os.getenv('NUCLIA_API_KEY')
KB_ID = os.getenv('NUCLIA_KB_ID')

if not API_KEY or not KB_ID:
    raise ValueError("Please set the NUCLIA_API_KEY and NUCLIA_KB_ID environment variables.")

# Base URL for your Knowledge Box
BASE_URL = f'https://{KB_ID}.nuclia.cloud/api/v1'

BASE_URL = f'https://europe-1.nuclia.cloud/api/v1/kb/903a0322-3d77-4ec3-94fd-3a10021c9500'

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
    payload = {'query': query}
    response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return None

def add_resource(title, content):
    """
    Add a new resource to the Knowledge Box.
    """
    url = f'{BASE_URL}/resources'
    payload = {
        'title': title,
        'content': content
    }
    response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 201:
        return response.json()
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return None

def get_resource(resource_id):
    """
    Retrieve a specific resource from the Knowledge Box by its ID.
    """
    url = f'{BASE_URL}/resources/{resource_id}'
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return None

if __name__ == '__main__':
    # Example usage:
    # Search the Knowledge Box
    search_results = search_knowledge_box('your_search_query')
    print(search_results)

    # Add a new resource
    new_resource = add_resource('Resource Title', 'Resource Content')
    print(new_resource)

    # Retrieve a specific resource by ID
    resource = get_resource('resource_id_here')
    print(resource)
