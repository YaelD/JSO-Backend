from typing import Any
from uuid import UUID

from sqlmodel import Session, select

from jso_backend.data_access.converters.job_converter import JobDBConverter
from jso_backend.data_access.dal_interfaces.job_data_access_interface import (
    IJobDataAccess,
)
from jso_backend.domain.exceptions.job_not_found_exception import JobNotFoundError
from jso_backend.domain.job_entity import JobEntity
from jso_backend.models.job_model import DBJobModel


class JobDataAccess(IJobDataAccess):
    def __init__(self, session: Session) -> None:
        self.db_session = session

    async def get_job_by_id(self, job_id: UUID) -> JobEntity:
        db_job: DBJobModel | None = self.db_session.get(DBJobModel, job_id)
        if not db_job:
            raise JobNotFoundError(id=job_id)
        job: JobEntity = JobDBConverter().convert_db_job_to_job_entity(db_job)
        return job

    async def get_list(self, limit: int = 0, offset: int = 0) -> list[JobEntity]:
        if limit == 0 and offset == 0:
            query = select(DBJobModel)
        elif limit != 0 and offset == 0:
            query = select(DBJobModel).limit(limit=limit)
        else:
            query = select(DBJobModel).limit(limit=limit).offset(offset=offset)
        db_jobs: list[DBJobModel] = self.db_session.exec(query).all()
        jobs: list[JobEntity] = []
        for db_job in db_jobs:
            jobs.append(JobDBConverter().convert_db_job_to_job_entity(db_job))
        return jobs

    async def create_job(self, job: JobEntity) -> JobEntity:
        db_job: DBJobModel = JobDBConverter().convert_job_entity_to_db_job(job)
        self.db_session.add(db_job)
        self.db_session.commit()
        self.db_session.refresh(db_job)
        job_entity: JobEntity = JobDBConverter().convert_db_job_to_job_entity(db_job)
        return job_entity

    async def update_job(self, job_id: UUID, job_data: dict[str, Any]) -> JobEntity:
        db_job: DBJobModel | None = self.db_session.get(DBJobModel, job_id)
        if not db_job:
            raise JobNotFoundError(id=job_id)
        for key, value in job_data.items():
            setattr(db_job, key, value)
        self.db_session.add(db_job)
        self.db_session.commit()
        self.db_session.refresh(db_job)
        updated_job: JobEntity = JobDBConverter().convert_db_job_to_job_entity(db_job)
        return updated_job

    def delete_job(self, job_id: UUID) -> None:
        db_job: DBJobModel | None = self.db_session.get(DBJobModel, job_id)
        if not db_job:
            raise JobNotFoundError(id=job_id)
        self.db_session.delete(db_job)
        self.db_session.commit()
