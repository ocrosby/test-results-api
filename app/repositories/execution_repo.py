from sqlmodel import Session, select

from app.models import TestExecution


class ExecutionRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_execution(self, execution: TestExecution):
        self.session.add(execution)
        self.session.commit()
        self.session.refresh(execution)
        return execution

    def get_execution_by_id(self, execution_id: int):
        return self.session.exec(
            select(TestExecution).where(TestExecution.id == execution_id)
        ).first()

    def get_all_executions(self):
        return self.session.exec(select(TestExecution)).all()

    def update_execution(self, execution: TestExecution):
        self.session.add(execution)
        self.session.commit()
        self.session.refresh(execution)
        return execution

    def delete_execution(self, execution_id: int):
        execution = self.get_execution_by_id(execution_id)
        if execution:
            self.session.delete(execution)
            self.session.commit()
        return execution
