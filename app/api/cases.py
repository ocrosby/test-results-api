from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.database import get_session
from app.services import TestCaseService

router = APIRouter()


@router.post("/")
def create_case(
    name: str, description: str, class_id: int, session: Session = Depends(get_session)
):
    try:
        case_service = TestCaseService(session)
        case = case_service.create_test_case(name, description, class_id)
        return {"message": "Case created successfully", "case_id": case.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/{case_id}")
def get_case(case_id: int, session: Session = Depends(get_session)):
    case_service = TestCaseService(session)
    case = case_service.get_test_case(case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case


@router.put("/{case_id}")
def update_case(
    case_id: int,
    name: str,
    description: str,
    class_id: int,
    session: Session = Depends(get_session),
):
    case_service = TestCaseService(session)
    case = case_service.update_test_case(case_id, name, description, class_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return {"message": "Case updated successfully"}


@router.delete("/{case_id}")
def delete_case(case_id: int, session: Session = Depends(get_session)):
    case_service = TestCaseService(session)
    case_service.delete_test_case(case_id)
    return {"message": "Case deleted successfully"}
