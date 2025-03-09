from typing import Optional
from sqlmodel import Field, SQLModel

class TestCase(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: Optional[str] = None
    class_id: int = Field(index=True)