from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.database import get_session
from app.services.suite_service import TestSuiteService

router = APIRouter()


@router.post("/")
def create_suite(name: str, description: str, session: Session = Depends(get_session)):
    try:
        suite_service = TestSuiteService(session)
        suite = suite_service.create_test_suite(name, description)
        return {"message": "Suite created successfully", "suite_id": suite.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/{suite_id}")
def get_suite(suite_id: int, session: Session = Depends(get_session)):
    suite_service = TestSuiteService(session)
    suite = suite_service.get_test_suite(suite_id)
    if not suite:
        raise HTTPException(status_code=404, detail="Suite not found")
    return suite


@router.put("/{suite_id}")
def update_suite(
    suite_id: int, name: str, description: str, session: Session = Depends(get_session)
):
    suite_service = TestSuiteService(session)
    suite = suite_service.update_test_suite(suite_id, name, description)
    if not suite:
        raise HTTPException(status_code=404, detail="Suite not found")
    return {"message": "Suite updated successfully"}


@router.delete("/{suite_id}")
def delete_suite(suite_id: int, session: Session = Depends(get_session)):
    suite_service = TestSuiteService(session)
    suite_service.delete_test_suite(suite_id)
    return {"message": "Suite deleted successfully"}
