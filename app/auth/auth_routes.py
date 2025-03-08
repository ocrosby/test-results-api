from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.database import get_session
from app.services import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register/")
def register(
    username: str, email: str, password: str, session: Session = Depends(get_session)
):
    try:
        auth_service = AuthService(session)
        user = auth_service.register_user(username, email, password)
        return {"message": "User registered successfully", "user_id": user.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.post("/login/")
def login(username: str, password: str, session: Session = Depends(get_session)):
    try:
        auth_service = AuthService(session)
        token = auth_service.login_user(username, password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e)) from e
