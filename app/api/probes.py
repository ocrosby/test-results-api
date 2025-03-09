from fastapi import APIRouter, Depends
from sqlmodel import Session

from app import get_session

router = APIRouter()


@router.get("/live", status_code=200)
def liveness_probe():
    """
    Liveness probe: Returns 200 if the service is running.
    """
    return {"status": "alive"}


@router.get("/ready", status_code=200)
def readiness_probe(session: Session = Depends(get_session)):
    """
    Readiness probe: Returns 200 if the database connection is alive.

    :param session: The database session.
    :return: A dictionary with the status of the database connection.
    """
    try:
        # Execute a simple query to check DB connectivity
        session.exec(r"SELECT 1")
        return {"status": "ready"}
    except Exception:
        return {"status": "not ready"}, 500


# 🚀 NEW: Startup Probe (checks if app has fully started)
@router.get("/startup", status_code=200)
def startup_probe():
    """
    Startup probe: Returns 200 if the app has started.

    :return: A dictionary with the status of the app.
    """
    return {"status": "started"}
