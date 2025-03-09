from sqlmodel import Session, select

from app.models import TestCase


class CaseRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_case(self, test_case: TestCase):
        self.session.add(test_case)
        self.session.commit()
        self.session.refresh(test_case)
        return test_case

    def get_case_by_id(self, case_id: int):
        return self.session.exec(select(TestCase).where(TestCase.id == case_id)).first()

    def get_all_cases(self):
        return self.session.exec(select(TestCase)).all()

    def update_case(self, test_case: TestCase):
        self.session.add(test_case)
        self.session.commit()
        self.session.refresh(test_case)
        return test_case

    def delete_case(self, case_id: int):
        test_case = self.get_case_by_id(case_id)
        if test_case:
            self.session.delete(test_case)
            self.session.commit()
        return test_case
