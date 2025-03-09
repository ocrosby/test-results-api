# python
from typing import List, Optional

from sqlmodel import Session

from app.models import TestSuite
from app.repositories.suite_repo import SuiteRepository


class TestSuiteService:
    def __init__(self, session: Session):
        self.suite_repo = SuiteRepository(session)

    def create_test_suite(self, name: str, description: str) -> TestSuite:
        test_suite = TestSuite(name=name, description=description)
        return self.suite_repo.create_suite(test_suite)

    def get_test_suite(self, suite_id: int) -> Optional[TestSuite]:
        return self.suite_repo.get_suite_by_id(suite_id)

    def get_test_suites(self) -> List[TestSuite]:
        return self.suite_repo.get_all_suites()

    def update_test_suite(
        self, suite_id: int, name: str, description: str
    ) -> Optional[TestSuite]:
        test_suite = self.suite_repo.get_suite_by_id(suite_id)
        if not test_suite:
            return None
        test_suite.name = name
        test_suite.description = description
        return self.suite_repo.update_suite(test_suite)

    def delete_test_suite(self, suite_id: int) -> bool:
        test_suite = self.suite_repo.get_suite_by_id(suite_id)
        if not test_suite:
            return False
        self.suite_repo.delete_suite(suite_id)
        return True
