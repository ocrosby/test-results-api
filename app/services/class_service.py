# python
from typing import List, Optional

from sqlmodel import Session

from app.models import TestClass
from app.repositories.class_repo import ClassRepository


class TestClassService:
    def __init__(self, session: Session):
        self.class_repo = ClassRepository(session)

    def create_test_class(self, name: str, description: str) -> TestClass:
        test_class = TestClass(name=name, description=description)
        return self.class_repo.create_class(test_class)

    def get_test_class(self, test_class_id: int) -> Optional[TestClass]:
        return self.class_repo.get_class_by_id(test_class_id)

    def get_test_classes(self) -> List[TestClass]:
        return self.class_repo.get_all_classes()

    def update_test_class(
        self, test_class_id: int, name: str, description: str
    ) -> Optional[TestClass]:
        test_class = self.class_repo.get_class_by_id(test_class_id)
        if not test_class:
            return None
        test_class.name = name
        test_class.description = description
        return self.class_repo.update_class(test_class)

    def delete_test_class(self, test_class_id: int) -> bool:
        test_class = self.class_repo.get_class_by_id(test_class_id)
        if not test_class:
            return False
        self.class_repo.delete_class(test_class)
        return True
