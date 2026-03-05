from typing import List, Tuple
from src.framework.core.base_client import BaseClient
from src.framework.models.pet import Pet

class PetService(BaseClient):
    def __init__(self):
        super().__init__()
        self.endpoint = "/pet"

    def add_pet(self, pet: Pet) -> Tuple[int, Pet]:
        response = self._request("POST", self.endpoint, json=pet.model_dump(exclude_none=True))
        return response.status_code, Pet.model_validate(response.json())

    def get_pet(self, pet_id: int) -> Tuple[int, Pet]:
        response = self._request("GET", f"{self.endpoint}/{pet_id}")
        return response.status_code, Pet.model_validate(response.json())

    def find_by_status(self, status: str) -> Tuple[int, List[Pet]]:
        response = self._request("GET", f"{self.endpoint}/findByStatus", params={"status": status})
        pets = [Pet.model_validate(p) for p in response.json()]
        return response.status_code, pets
