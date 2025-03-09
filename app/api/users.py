from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.database import get_session
from app.services import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(
    username: str, email: str, password: str, session: Session = Depends(get_session)
):
    try:
        user_service = UserService(session)
        user = user_service.create_user(username, email, password)
        return {"message": "User created successfully", "user_id": user.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_session)):
    user_service = UserService(session)
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}")
def update_user(
    user_id: int, username: str, email: str, session: Session = Depends(get_session)
):
    user_service = UserService(session)
    user = user_service.update_user(user_id, username, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}


@router.delete("/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user_service = UserService(session)
    user_service.delete_user(user_id)
    return {"message": "User deleted successfully"}
