from jso_backend.data_access.converters.process_step_converter import (
    ProcessStepDBConverter,
)
from jso_backend.domain.job_entity import JobEntity
from jso_backend.domain.job_process import JobProcess
from jso_backend.models.job_model import DBJobModel


class JobDBConverter:
    def convert_db_job_to_job_entity(self, job: DBJobModel) -> JobEntity:
        return JobEntity(
            company_name=job.company_name,
            role=job.role,
            status=job.status,
            creation_date=job.creation_date,
            job_link=job.job_link,
            about=job.about,
            tech_stack=job.tech_stack,
            id=job.id,
            process_steps=JobProcess(
                ProcessStepDBConverter().convert_list_of_dicts_to_process_step_entity_list(
                    job.process_steps
                ),
            ),
        )

    def convert_job_entity_to_db_job(self, job: JobEntity) -> DBJobModel:
        return DBJobModel(
            creation_date=job.creation_date,
            company_name=job.company_name,
            role=job.role,
            status=job.status,
            job_link=job.job_link,
            about=job.about,
            tech_stack=job.tech_stack,
            process_steps=ProcessStepDBConverter().convert_list_of_process_step_entity_to_list_of_dict(
                job_process=job.process_steps
            ),
            id=job.id if job.id else None,
        )
