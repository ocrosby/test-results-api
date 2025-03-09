from typing import List, Optional

from sqlmodel import Session

from app.models import TestExecution
from app.repositories.execution_repo import ExecutionRepository


class TestExecutionService:
    def __init__(self, session: Session):
        self.execution_repo = ExecutionRepository(session)

    def create_test_execution(
        self, name: str, status: str, suite_id: int
    ) -> TestExecution:
        test_execution = TestExecution(name=name, status=status, suite_id=suite_id)
        return self.execution_repo.create_execution(test_execution)

    def get_test_execution(self, test_execution_id: int) -> Optional[TestExecution]:
        return self.execution_repo.get_execution_by_id(test_execution_id)

    def get_test_executions(self) -> List[TestExecution]:
        return self.execution_repo.get_all_executions()

    def update_test_execution(
        self, test_execution_id: int, name: str, status: str, suite_id: int
    ) -> Optional[TestExecution]:
        test_execution = self.execution_repo.get_execution_by_id(test_execution_id)
        if not test_execution:
            return None
        test_execution.name = name
        test_execution.status = status
        test_execution.suite_id = suite_id
        return self.execution_repo.update_execution(test_execution)

    def delete_test_execution(self, test_execution_id: int) -> bool:
        test_execution = self.execution_repo.get_execution_by_id(test_execution_id)
        if not test_execution:
            return False
        self.execution_repo.delete_execution(test_execution)
        return True
