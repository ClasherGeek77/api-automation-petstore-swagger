from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class Pet(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    
    id: Optional[int] = None
    category: Optional[Category] = None
    name: str
    photoUrls: List[str]
    tags: Optional[List[Tag]] = None
    status: Optional[str] = None
