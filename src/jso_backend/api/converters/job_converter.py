from jso_backend.api.converters.process_steps_converter import ProcessStepConverter
from jso_backend.api.models.job_api_model import JobReceive, JobSend
from jso_backend.domain.job_entity import JobEntity


class JobConverter:
    def from_job_api_to_job_entity(self, job_api: JobReceive) -> JobEntity:
        return JobEntity(
            company_name=job_api.company_name,
            role=job_api.role,
            status=job_api.status,
            creation_date=job_api.creation_date,
            job_link=job_api.job_link,
            about=job_api.about,
            tech_stack=job_api.tech_stack,
        )

    def from_job_entity_to_job_api(self, job_entity: JobEntity) -> JobSend:
        return JobSend(
            company_name=job_entity.company_name,
            role=job_entity.role,
            status=job_entity.status,
            creation_date=job_entity.creation_date,
            job_link=job_entity.job_link,
            about=job_entity.about,
            tech_stack=job_entity.tech_stack,
            id=job_entity.id,  # type: ignore
            process_steps=ProcessStepConverter().convert_process_step_entity_to_process_step_api(
                job_entity.process_steps.process_steps
            ),
        )
