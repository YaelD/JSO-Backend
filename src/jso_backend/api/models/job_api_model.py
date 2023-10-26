from datetime import datetime
from typing import Any

from pydantic import BaseModel, root_validator

from jso_backend.api.models.process_step_api_model import ProcessStepApiModel
from jso_backend.domain.job_status_type import JobStatus


class JobBase(BaseModel):
    creation_date: datetime | None = datetime.now()
    company_name: str
    role: str
    status: JobStatus = JobStatus.PENDING
    job_link: str | None = None
    about: str | None = None
    tech_stack: list[str] = []


class JobReceive(JobBase):
    @root_validator
    def check_required_fields_are_not_empty_string(cls, values: dict[str, Any]) -> dict[str, Any]:
        role, company_name = values.get("role"), values.get("company_name")
        if role == "" or company_name == "":
            raise ValueError("role and company_name filed can not be empty")
        return values


class JobSend(JobBase):
    id: int
    process_steps: list[ProcessStepApiModel]


class JobUpdate(BaseModel):
    creation_date: datetime | None = None
    company_name: str | None = None
    role: str | None = None
    status: JobStatus | None = None
    job_link: str | None = None
    about: str | None = None
    tech_stack: list[str] | None = None
    process_steps: list[ProcessStepApiModel] | None = None
