from typing import Any

from jso_backend.business_logic.logic.job_logic import JobLogic
from jso_backend.business_logic.validators.job_validator import JobValidator
from jso_backend.data_access.job_data_access import JobDataAccess
from jso_backend.data_access.unit_of_work import UnitOfWork
from jso_backend.domain.job_entity import JobEntity
from jso_backend.domain.job_process import JobProcess


class JobService:
    async def get_job_by_id(self, id: int) -> JobEntity:
        async with UnitOfWork().create() as unit_of_work:
            job: JobEntity = await JobDataAccess(session=unit_of_work).get_job_by_id(job_id=id)
            return job

    async def get_all_jobs(self) -> list[JobEntity]:
        async with UnitOfWork().create() as unit_of_work:
            all_jobs: list[JobEntity] = await JobDataAccess(unit_of_work).get_list()
            return all_jobs

    async def create_job(self, job: JobEntity) -> JobEntity:
        async with UnitOfWork().create() as unit_of_work:
            created_job: JobEntity = await JobDataAccess(unit_of_work).create_job(job)
            return created_job

    async def update_job(
        self, id: int, job_details: dict[str, Any], job_process: JobProcess | None = None
    ) -> JobEntity:
        async with UnitOfWork().create() as unit_of_work:
            job_access_data: JobDataAccess = JobDataAccess(unit_of_work)
            job_to_update: JobEntity = await job_access_data.get_job_by_id(job_id=id)
            JobValidator(
                job_entity=job_to_update,
                job_details_to_update=job_details,
                job_process=job_process,
            ).validate_job_data_fields()
            JobLogic().update_job_details(job_to_update, job_details, job_process)
            updated_job: JobEntity = await job_access_data.update_job(
                job_id=id, job_data=job_details
            )
            return updated_job

    async def delete_job_by_id(self, id: int) -> None:
        async with UnitOfWork().create() as unit_of_work:
            job_data_access: JobDataAccess = JobDataAccess(session=unit_of_work)
            await job_data_access.get_job_by_id(job_id=id)
            job_data_access.delete_job(job_id=id)
