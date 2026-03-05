import requests
import uuid
import logging

logger = logging.getLogger(__name__)

BASE_URL = "https://petstore.swagger.io/v2"

def create_pet(name, status="available"):
    pet_id = uuid.uuid4().int >> 64
    payload = {
        "id": pet_id,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": name,
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": status
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    try:
        data = response.json()
    except ValueError:
        data = response.text
    logger.info(f"[create_pet] Status: {response.status_code}, Response: {data}")
    return response.status_code, data

def get_pet_by_id(pet_id):
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    try:
        data = response.json()
    except ValueError:
        data = response.text
    logger.info(f"[get_pet_by_id] Status: {response.status_code}, Response: {data}")
    return response.status_code, data

def find_pets_by_status(status):
    response = requests.get(f"{BASE_URL}/pet/findByStatus", params={"status": status})
    try:
        data = response.json()
    except ValueError:
        data = response.text
    logger.info(f"[find_pets_by_status] Status: {response.status_code}, Response: {str(data)[:500]}")  # limit large output
    return response.status_code, data
