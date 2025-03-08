import pytest
from sqlmodel import Session
from app.models import User
from app.repositories.user_repo import UserRepository

@pytest.fixture
def mock_session(mocker):
    return mocker.MagicMock(spec=Session)

def test_create_user(mock_session):
    user_repo = UserRepository(mock_session)
    user = User(username="testuser", email="test@example.com", password="password")

    mock_session.add.return_value = None
    mock_session.commit.return_value = None
    mock_session.refresh.return_value = None

    created_user = user_repo.create_user(user)

    mock_session.add.assert_called_once_with(user)
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(user)
    assert created_user == user

def test_get_user_by_username(mock_session):
    user_repo = UserRepository(mock_session)
    user = User(username="testuser", email="test@example.com", password="password")

    mock_session.exec.return_value.first.return_value = user

    result = user_repo.get_user_by_username("testuser")

    mock_session.exec.assert_called_once()
    assert result == user

def test_get_user_by_email(mock_session):
    user_repo = UserRepository(mock_session)
    user = User(username="testuser", email="test@example.com", password="password")

    mock_session.exec.return_value.first.return_value = user

    result = user_repo.get_user_by_email("test@example.com")

    mock_session.exec.assert_called_once()
    assert result == user