# python
from typing import List, Optional

from sqlmodel import Session

from app.models import TestCase
from app.repositories.case_repo import CaseRepository


class TestCaseService:
    def __init__(self, session: Session):
        self.case_repo = CaseRepository(session)

    def create_test_case(self, name: str, description: str, class_id: int) -> TestCase:
        test_case = TestCase(name=name, description=description, class_id=class_id)
        return self.case_repo.create_case(test_case)

    def get_test_case(self, test_case_id: int) -> Optional[TestCase]:
        return self.case_repo.get_case_by_id(test_case_id)

    def get_test_cases(self) -> List[TestCase]:
        return self.case_repo.get_all_cases()

    def update_test_case(
        self, test_case_id: int, name: str, description: str, class_id: int
    ) -> Optional[TestCase]:
        test_case = self.case_repo.get_case_by_id(test_case_id)
        if not test_case:
            return None
        test_case.name = name
        test_case.description = description
        test_case.class_id = class_id
        return self.case_repo.update_case(test_case)

    def delete_test_case(self, test_case_id: int) -> bool:
        test_case = self.case_repo.get_case_by_id(test_case_id)
        if not test_case:
            return False
        self.case_repo.delete_case(test_case)
        return True
