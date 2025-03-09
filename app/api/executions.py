from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.database import get_session
from app.services.execution_service import TestExecutionService

router = APIRouter()


@router.post("/")
def create_execution(
    name: str, description: str, case_id: int, session: Session = Depends(get_session)
):
    try:
        execution_service = TestExecutionService(session)
        execution = execution_service.create_test_execution(name, description, case_id)
        return {
            "message": "Execution created successfully",
            "execution_id": execution.id,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/{execution_id}")
def get_execution(execution_id: int, session: Session = Depends(get_session)):
    execution_service = TestExecutionService(session)
    execution = execution_service.get_test_execution(execution_id)
    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")
    return execution


@router.put("/{execution_id}")
def update_execution(
    execution_id: int,
    name: str,
    description: str,
    case_id: int,
    session: Session = Depends(get_session),
):
    execution_service = TestExecutionService(session)
    execution = execution_service.update_test_execution(
        execution_id, name, description, case_id
    )
    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")
    return {"message": "Execution updated successfully"}


@router.delete("/{execution_id}")
def delete_execution(execution_id: int, session: Session = Depends(get_session)):
    execution_service = TestExecutionService(session)
    execution_service.delete_test_execution(execution_id)
    return {"message": "Execution deleted successfully"}
