from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict

class Environment(str, Enum):
    PROD = "prod"
    STAGING = "staging"
    DEV = "dev"

class Settings(BaseSettings):
    env: Environment = Environment.PROD
    base_url: str = "https://petstore.swagger.io/v2"
    timeout: int = 30
    
    # Model config
    model_config = SettingsConfigDict(
        env_prefix="API_TEST_",
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
