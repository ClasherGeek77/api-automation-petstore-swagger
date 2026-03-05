import pytest
import uuid
from src.framework.models.pet import Pet

def test_add_new_pet(pet_service):
    pet_name = f"Cat_{uuid.uuid4().hex[:6]}"
    pet_data = Pet(name=pet_name, photoUrls=["http://example.com/cat.jpg"])
    
    status_code, pet = pet_service.add_pet(pet_data)
    
    assert status_code == 200
    assert pet.name == pet_name
    assert pet.id is not None

def test_find_by_status_available(pet_service):
    status_code, pets = pet_service.find_by_status("available")
    assert status_code == 200
    assert len(pets) > 0
    assert all(p.status == "available" for p in pets)

def test_get_existing_pet(pet_service):
    # Setup: Create a pet first to ensure it exists
    pet_name = "ToGet"
    pet_data = Pet(name=pet_name, photoUrls=[])
    _, created_pet = pet_service.add_pet(pet_data)
    
    status_code, pet = pet_service.get_pet(created_pet.id)
    assert status_code == 200
    assert pet.id == created_pet.id
    assert pet.name == pet_name
