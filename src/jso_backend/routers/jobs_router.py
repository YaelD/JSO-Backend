from typing import Any, Generator

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from jso_backend.api_models.job_dto import JobReceive, JobSend, JobUpdate
from jso_backend.business_logic.job_entity import JobEntity
from jso_backend.models.job_model import DBJobModel
from jso_backend.models.process_step_model import DBProcessStepModel

from ..data_access.database_manager import DatabaseManager
from ..data_access.job_data_access import JobDataAccess

router = APIRouter(prefix="/jobs", tags=["jobs"])


def get_db_session() -> Generator[Session, Any, Any]:
    session: Session = DatabaseManager().get_session()
    try:
        yield session
    finally:
        session.close()


@router.get("/", response_model=list[JobSend])
async def get_list_of_jobs(db_session: Session = Depends(get_db_session)):
    return JobDataAccess(db_session).get_list()


@router.get("/{job_id}", response_model=JobSend)
async def get_job(job_id: int, db_session: Session = Depends(get_db_session)):
    db_job: DBJobModel | None = JobDataAccess(db_session).get_job(job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job


@router.post("/", response_model=JobSend)
async def create_job(job: JobReceive, db_session: Session = Depends(get_db_session)):
    new_job: JobEntity = JobEntity(**job.dict())
    new_db_job: DBJobModel = new_job.convert_to_DBJobModel()
    starting_steps: list[
        DBProcessStepModel
    ] = new_job.process_steps.convert_process_steps_to_DBProcessSteps(new_db_job)
    return JobDataAccess(db_session).create_job(job=job.dict(), starting_steps=starting_steps)


@router.patch("/{job_id}", response_model=JobSend)
async def update_job(job_id: int, job: JobUpdate, db_session: Session = Depends(get_db_session)):
    job_access_data: JobDataAccess = JobDataAccess(db_session)
    db_job: DBJobModel | None = job_access_data.get_job(job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Invalid job id. Job not found")
    new_job: JobEntity = JobEntity.convert_from_DBJobModel(db_job)
    new_job.validate_and_update_job_data_fields(job.dict(exclude_unset=True))
    return job_access_data.update_job(db_job, job_data=job.dict(exclude_unset=True))


@router.delete("/{job_id}")
async def delete_job(job_id: int, db_session: Session = Depends(get_db_session)):
    job_access_data: JobDataAccess = JobDataAccess(db_session)
    db_job: DBJobModel | None = job_access_data.get_job(job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    job_access_data.delete_job(db_job)
