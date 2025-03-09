from sqlmodel import Session, select

from app.models import TestSuite


class SuiteRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_suite(self, suite: TestSuite):
        self.session.add(suite)
        self.session.commit()
        self.session.refresh(suite)
        return suite

    def get_suite_by_id(self, suite_id: int):
        return self.session.exec(
            select(TestSuite).where(TestSuite.id == suite_id)
        ).first()

    def get_all_suites(self):
        return self.session.exec(select(TestSuite)).all()

    def update_suite(self, suite: TestSuite):
        self.session.add(suite)
        self.session.commit()
        self.session.refresh(suite)
        return suite

    def delete_suite(self, suite_id: int):
        suite = self.get_suite_by_id(suite_id)
        if suite:
            self.session.delete(suite)
            self.session.commit()
        return suite
