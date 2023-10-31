from uuid import UUID

from fastapi import APIRouter, HTTPException

from jso_backend.api.converters.job_converter import JobConverter
from jso_backend.api.converters.process_steps_converter import ProcessStepConverter
from jso_backend.api.models.job_api_model import JobReceive, JobSend, JobUpdate
from jso_backend.business_logic.services.job_service import JobService
from jso_backend.domain.exceptions.invalid_job_details_exception import (
    InvalidJobDetailsError,
)
from jso_backend.domain.exceptions.job_not_found_exception import JobNotFoundError
from jso_backend.domain.job_entity import JobEntity
from jso_backend.domain.process_step_entity import ProcessStepEntity

# from jso_backend.domain.job_process import JobProcess

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model=list[JobSend])
async def get_list_of_jobs():
    all_jobs: list[JobEntity] = await JobService().get_all_jobs()
    jobs: map[JobSend] = map(lambda job: JobConverter().from_job_entity_to_job_api(job), all_jobs)
    return list(jobs)


@router.get("/{job_id}", response_model=JobSend)
async def get_job(job_id: UUID):
    try:
        job_entity: JobEntity = await JobService().get_job_by_id(id=job_id)
        job: JobSend = JobConverter().from_job_entity_to_job_api(job_entity=job_entity)
        return job
    except JobNotFoundError as error:
        raise HTTPException(status_code=404, detail=error.message)


@router.post("/", response_model=JobSend)
async def create_job(job: JobReceive):
    job_entity: JobEntity = JobConverter().from_job_api_to_job_entity(job_api=job)
    created_job: JobEntity = await JobService().create_job(job=job_entity)
    job_to_send: JobSend = JobConverter().from_job_entity_to_job_api(created_job)
    return job_to_send


@router.patch("/{job_id}", response_model=JobSend)
async def update_job(job_id: UUID, job: JobUpdate):
    try:
        process_steps_to_update: list[ProcessStepEntity] | None = None
        if job.process_steps is not None:
            process_steps_to_update = (
                ProcessStepConverter().convert_dict_process_step_list_to_job_process(
                    job.process_steps
                )
            )
        updated_job: JobEntity = await JobService().update_job(
            id=job_id,
            job_details=job.dict(exclude_unset=True),
            process_steps=process_steps_to_update,
        )
        job_send: JobSend = JobConverter().from_job_entity_to_job_api(updated_job)
        return job_send
    except JobNotFoundError as error:
        raise HTTPException(status_code=404, detail=error.message)
    except InvalidJobDetailsError as error:
        raise HTTPException(status_code=400, detail=error.message)


@router.delete("/{job_id}")
async def delete_job(job_id: UUID):
    try:
        await JobService().delete_job_by_id(job_id)
    except JobNotFoundError as error:
        raise HTTPException(status_code=404, detail=error.message)
