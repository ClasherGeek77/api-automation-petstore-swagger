import pytest
import logging
from src.framework.services.pet_service import PetService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@pytest.fixture(scope="session")
def pet_service():
    return PetService()
