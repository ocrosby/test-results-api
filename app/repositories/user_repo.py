from sqlmodel import Session, select
from app.models.user import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user_by_username(self, username: str):
        return self.session.exec(select(User).where(User.username == username)).first()

    def get_user_by_email(self, email: str):
        return self.session.exec(select(User).where(User.email == email)).first()