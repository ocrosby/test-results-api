from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.database import get_session
from app.services.class_service import TestClassService

router = APIRouter()


@router.post("/")
def create_class(name: str, description: str, session: Session = Depends(get_session)):
    try:
        class_service = TestClassService(session)
        class_ = class_service.create_test_class(name, description)
        return {"message": "Class created successfully", "class_id": class_.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/{class_id}")
def get_class(class_id: int, session: Session = Depends(get_session)):
    class_service = TestClassService(session)
    class_ = class_service.get_test_class(class_id)
    if not class_:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_


@router.put("/{class_id}")
def update_class(
    class_id: int, name: str, description: str, session: Session = Depends(get_session)
):
    class_service = TestClassService(session)
    class_ = class_service.update_test_class(class_id, name, description)
    if not class_:
        raise HTTPException(status_code=404, detail="Class not found")
    return {"message": "Class updated successfully"}


@router.delete("/{class_id}")
def delete_class(class_id: int, session: Session = Depends(get_session)):
    class_service = TestClassService(session)
    class_service.delete_test_class(class_id)
    return {"message": "Class deleted successfully"}
