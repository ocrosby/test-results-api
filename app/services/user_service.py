from sqlmodel import Session

from app.core.security import hash_password
from app.models import User
from app.repositories import UserRepository


class UserService:
    def __init__(self, session: Session):
        self.user_repo = UserRepository(session)

    def create_user(self, username: str, email: str, password: str) -> User:
        if self.user_repo.get_user_by_username(username):
            raise ValueError("Username already exists")

        if self.user_repo.get_user_by_email(email):
            raise ValueError("Email already in use")

        user = User(
            username=username, email=email, password_hash=hash_password(password)
        )

        return self.user_repo.create_user(user)

    def get_user(self, user_id: int) -> User:
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def update_user(self, user_id: int, username: str, email: str) -> User:
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        user.username = username
        user.email = email

        return self.user_repo.update_user(user)

    def delete_user(self, user_id: int) -> None:
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        self.user_repo.delete_user(user)
