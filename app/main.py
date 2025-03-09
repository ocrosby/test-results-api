from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import cases, classes, executions, probes, suites
from app.core.database import create_db_and_tables

# Initialize FastAPI app
api = FastAPI(title="Test Results API")

# CORS Middleware
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@asynccontextmanager
async def lifespan(my_app: FastAPI):
    # Startup event
    create_db_and_tables()
    yield
    # Shutdown event
    # Add any necessary cleanup code here


api.router.lifespan_context = lifespan


# Include API routers
api.include_router(suites.router, prefix="/test-suites", tags=["Test Suites"])
api.include_router(classes.router, prefix="/test-classes", tags=["Test Classes"])
api.include_router(cases.router, prefix="/test-cases", tags=["Test Cases"])
api.include_router(
    executions.router, prefix="/test-executions", tags=["Test Executions"]
)
api.include_router(probes.router, prefix="/healthz", tags=["Kubernetes Probes"])
