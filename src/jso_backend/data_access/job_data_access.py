from typing import Any

from sqlmodel import Session, select

from jso_backend.models.job_model import DBJobModel
from jso_backend.models.process_step_model import DBProcessStepModel


class JobDataAccess:
    def __init__(self, session: Session) -> None:
        self.db_session = session

    def get_job(self, job_id: int) -> DBJobModel | None:
        db_job = self.db_session.get(DBJobModel, job_id)
        return db_job

    def get_list(self, limit: int = 0, offset: int = 0) -> list[DBJobModel]:
        if limit == 0 and offset == 0:
            query = select(DBJobModel)
        elif limit != 0 and offset == 0:
            query = select(DBJobModel).limit(limit=limit)
        else:
            query = select(DBJobModel).limit(limit=limit).offset(offset=offset)
        return self.db_session.exec(query).all()

    def create_job(
        self, job: dict[str, Any], starting_steps: list[DBProcessStepModel]
    ) -> DBJobModel:
        db_job: DBJobModel = DBJobModel(**job)
        db_job.process_steps = starting_steps
        self.db_session.add(db_job)
        self.db_session.commit()
        self.db_session.refresh(db_job)
        return db_job

    def update_job(self, db_job: DBJobModel, job_data: dict[str, Any]) -> DBJobModel:
        print("JOB DATA====>", job_data)
        for key, value in job_data.items():
            setattr(db_job, key, value)
        print(db_job.dict())
        self.db_session.add(db_job)
        self.db_session.commit()
        self.db_session.refresh(db_job)
        return db_job

    def delete_job(self, db_job: DBJobModel) -> None:
        self.db_session.delete(db_job)
        self.db_session.commit()
