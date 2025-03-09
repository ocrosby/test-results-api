from sqlmodel import Session, select

from app.models import TestClass


class ClassRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_class(self, test_class: TestClass):
        self.session.add(test_class)
        self.session.commit()
        self.session.refresh(test_class)
        return test_class

    def get_class_by_id(self, class_id: int):
        return self.session.exec(
            select(TestClass).where(TestClass.id == class_id)
        ).first()

    def get_all_classes(self):
        return self.session.exec(select(TestClass)).all()

    def update_class(self, test_class: TestClass):
        self.session.add(test_class)
        self.session.commit()
        self.session.refresh(test_class)
        return test_class

    def delete_class(self, class_id: int):
        test_class = self.get_class_by_id(class_id)
        if test_class:
            self.session.delete(test_class)
            self.session.commit()
        return test_class
