from src.framework.services.pet_service import PetService
from src.framework.models.pet import Pet
import pytest

def test_contract_get_pet_invalid_id(pet_service):
    """
    Contract test: Verify that a non-existent pet ID returns an error 
    but the response (if any) still adheres to expected error formats.
    """
    # Petstore returns 404 for non-existent IDs
    status_code, _ = pet_service.get_pet(999999999)
    assert status_code == 404

def test_contract_pet_schema_validation():
    """
    Verify our Pydantic model correctly validates valid data
    and rejects invalid data structures (contract simulation).
    """
    valid_data = {
        "id": 1,
        "name": "Doggy",
        "photoUrls": ["url1"],
        "status": "available"
    }
    pet = Pet.model_validate(valid_data)
    assert pet.name == "Doggy"
    
    with pytest.raises(Exception):
        # Missing required field 'photoUrls'
        Pet.model_validate({"name": "NoPhoto"})
