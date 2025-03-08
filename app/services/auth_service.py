from sqlmodel import Session
from app.repositories.user_repo import UserRepository
from app.core.security import hash_password, verify_password
from app.auth.auth_handler import create_access_token
from app.models import User
from datetime import timedelta

class AuthService:
    def __init__(self, session: Session):
        self.user_repo = UserRepository(session)

    def register_user(self, username: str, email: str, password: str):
        if self.user_repo.get_user_by_username(username):
            raise ValueError("Username already exists")
        if self.user_repo.get_user_by_email(email):
            raise ValueError("Email already in use")

        user = User(username=username, email=email, password_hash=hash_password(password))
        return self.user_repo.create_user(user)

    def login_user(self, username: str, password: str):
        user = self.user_repo.get_user_by_username(username)
        if not user or not verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")

        return create_access_token({"sub": user.username}, expires_delta=timedelta(minutes=30))