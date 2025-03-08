import pytest
from sqlmodel import Session

from app.core.database import engine, get_session


def test_get_session(mocker):
    """
    Test the get_session function to ensure it creates and yields a session correctly.
    """
    # Arrange
    # Mock the Session class
    mock_session = mocker.patch("app.core.database.Session", autospec=True)
    # Mock the engine
    mock_engine = mocker.patch("app.core.database.engine", autospec=True)
    # Create a mock session instance
    mock_session_instance = mock_session.return_value.__enter__.return_value

    # Act
    # Call the get_session function
    session_generator = get_session()
    session = next(session_generator)

    # Assert
    # Assert that the session is created with the engine
    mock_session.assert_called_once_with(mock_engine)
    # Assert that the session is yielded
    assert session == mock_session_instance
    # Close the session
    with pytest.raises(StopIteration):
        next(session_generator)
