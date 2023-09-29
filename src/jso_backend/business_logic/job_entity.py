from datetime import datetime
from typing import Any

from jso_backend.business_logic.job_process import JobProcess
from jso_backend.common.job_status_type import JobStatus
from jso_backend.models.job_model import DBJobModel


class JobEntity:
    def __init__(
        self,
        company_name: str,
        role: str,
        status: JobStatus = JobStatus.PENDING,
        creation_date: datetime | None = datetime.now(),
        job_link: str | None = "",
        about: str | None = "",
        tech_stack: list[str] = [],
        process_steps: JobProcess = JobProcess(),
    ):
        self.creation_date = creation_date
        self.company_name = company_name
        self.role = role
        self.status = status
        self.job_link = job_link
        self.about = about
        self.tech_stack = tech_stack
        self.process_steps = process_steps

    @classmethod
    def convert_from_DBJobModel(cls, db_job: DBJobModel) -> "JobEntity":
        return cls(
            company_name=db_job.company_name,
            role=db_job.role,
            status=db_job.status,
            creation_date=db_job.creation_date,
            job_link=db_job.job_link,
            about=db_job.about,
            tech_stack=db_job.tech_stack,
        )

    def convert_to_DBJobModel(self) -> DBJobModel:
        return DBJobModel(
            company_name=self.company_name,
            role=self.role,
            status=self.status,
            creation_date=self.creation_date,
            job_link=self.job_link,
            about=self.about,
            tech_stack=self.tech_stack,
            curr_step_id=None,
        )

    def validate_and_update_job_data_fields(self, job_details_to_update: dict[Any, Any]) -> None:
        self.validate_role_and_company_name(job_details_to_update)
        status: JobStatus | None = job_details_to_update.get("status")
        if status:
            updated_value: JobStatus = self.validate_status(status)
            job_details_to_update["status"] = updated_value

    def validate_role_and_company_name(self, job_details: dict[str, Any]) -> None:
        company_name: str | None = job_details.get("company_name")
        if company_name and company_name == "":
            job_details["company_name"] = self.company_name
        role: str | None = job_details.get("role")
        if role and role == "":
            job_details["role"] = self.role

    def validate_status(self, value: JobStatus) -> JobStatus:
        if value is JobStatus.CLOSE:
            return value
        elif value is JobStatus.OPEN:
            return (
                JobStatus.OPEN
                if self.process_steps.process_steps[2].is_completed
                else JobStatus.PENDING
            )
        else:  # value is JobStatus.Pending
            return self.status
