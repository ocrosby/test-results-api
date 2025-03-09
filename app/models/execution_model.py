from typing import Optional
from sqlmodel import Field, SQLModel

class TestExecution(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    suite_id: int = Field(index=True)
    status: str
    start_time: Optional[str] = None
    end_time: Optional[str] = None