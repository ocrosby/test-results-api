from fastapi import FastAPI
from app.api import test_suites, test_classes, test_cases, test_executions, probes
from app.core.database import create_db_and_tables

# Initialize FastAPI app
app = FastAPI(title="Test Results API")

# Database Initialization
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include API routers
app.include_router(test_suites.router, prefix="/test-suites", tags=["Test Suites"])
app.include_router(test_classes.router, prefix="/test-classes", tags=["Test Classes"])
app.include_router(test_cases.router, prefix="/test-cases", tags=["Test Cases"])
app.include_router(test_executions.router, prefix="/test-executions", tags=["Test Executions"])
app.include_router(probes.router, prefix="/healthz", tags=["Kubernetes Probes"])