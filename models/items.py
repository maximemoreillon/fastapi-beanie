from beanie import Document
from typing import Optional


class Item(Document):
    name: str
    description: Optional[str] = None
