from typing import Any

from jso_backend.domain.job_entity import JobEntity
from jso_backend.domain.job_status_type import JobStatus


class JobValidator:
    def validate_and_update_job_data_fields(
        self, job_entity: JobEntity, job_details_to_update: dict[Any, Any]
    ) -> None:
        self.validate_role_and_company_name(
            job_entity=job_entity, job_details=job_details_to_update
        )
        status: JobStatus | None = job_details_to_update.get("status")
        if status:
            updated_value: JobStatus = self.validate_status(job_entity=job_entity, value=status)
            job_details_to_update["status"] = updated_value

    def validate_role_and_company_name(
        self, job_entity: JobEntity, job_details: dict[str, Any]
    ) -> None:
        company_name: str | None = job_details.get("company_name")
        if company_name and company_name == "":
            job_details["company_name"] = job_entity.company_name
        role: str | None = job_details.get("role")
        if role and role == "":
            job_details["role"] = job_entity.role

    def validate_status(self, job_entity: JobEntity, value: JobStatus) -> JobStatus:
        if value is JobStatus.CLOSE:
            return value
        elif value is JobStatus.OPEN:
            return (
                JobStatus.OPEN
                if job_entity.process_steps.process_steps[2].is_completed
                else JobStatus.PENDING
            )
        else:  # value is JobStatus.Pending
            return job_entity.status
