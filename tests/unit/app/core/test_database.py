import os

import pytest
from sqlmodel import Session

from app.core.database import get_engine, get_session


@pytest.fixture
def mock_get_engine(mocker):
    return mocker.patch("app.core.database.get_engine", autospec=True)


@pytest.fixture
def mock_session(mocker):
    return mocker.patch("app.core.database.Session", autospec=True)


def test_get_session(mock_get_engine, mock_session):
    """
    Test the get_session function to ensure it creates and yields a session correctly.
    """
    # Arrange
    # Set the DATABASE_URL environment variable
    os.environ["DATABASE_URL"] = "sqlite:///test.db"

    # Ensure the mock get_engine returns a mock engine
    mock_engine_instance = mock_get_engine.return_value
    # Create a mock session instance
    mock_session_instance = mock_session.return_value.__enter__.return_value

    # Ensure mock_session_instance is not None
    assert mock_session_instance is not None, "Mock session instance is None"

    # Act
    # Call the get_session function
    session_generator = get_session()
    session = next(session_generator)

    # Assert
    # Assert that the session is created with the engine
    mock_get_engine.assert_called_once()
    mock_session.assert_called_once_with(mock_engine_instance)
    # Assert that the session is yielded
    assert session == mock_session_instance
    # Close the session
    with pytest.raises(StopIteration):
        next(session_generator)
