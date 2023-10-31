import uuid
from datetime import date
from typing import Any

from pydantic import BaseModel, Field, root_validator, validator

from jso_backend.api.models.process_step_api_model import ProcessStepApiModel
from jso_backend.domain.job_status_type import JobStatus


class JobBase(BaseModel):
    creation_date: date | None = date.today()
    company_name: str = Field(min_length=1, max_length=50)
    role: str = Field(min_length=1, max_length=50)
    status: JobStatus = JobStatus.PENDING
    job_link: str | None = None
    about: str | None = None
    tech_stack: list[str] = []

    @validator("creation_date")
    @classmethod
    def validate_creation_date(cls, value: date) -> date:
        if value > date.today():
            raise ValueError("Invalid creation date. Creation date can not be a future date")
        return value


class JobReceive(JobBase):
    @validator("role", "company_name")
    @classmethod
    def check_required_fields_are_not_empty_string(cls, value: str) -> str:
        if value == "":
            raise ValueError("role and company_name filed can not be empty")
        return value


class JobSend(JobBase):
    id: uuid.UUID
    process_steps: list[ProcessStepApiModel]


class JobUpdate(BaseModel):
    creation_date: date | None = None
    company_name: str | None = None
    role: str | None = None
    status: JobStatus | None = None
    job_link: str | None = None
    about: str | None = None
    tech_stack: list[str] | None = None
    process_steps: list[ProcessStepApiModel] | None = None

    @validator("process_steps")
    def validate_process_steps(cls, value: list[ProcessStepApiModel]) -> list[ProcessStepApiModel]:
        if len(value) < 3:
            raise ValueError("Invalid process steps. Process steps must contain 3 starting steps")
        return value

    @root_validator
    def validate_process_steps_and_status(cls, values: dict[str, Any]) -> dict[str, Any]:
        process_steps: list[ProcessStepApiModel] | None = values.get("process_steps")
        status: JobStatus | None = values.get("status")
        if process_steps and status:
            if process_steps[2].is_completed == True and status == JobStatus.PENDING:
                raise ValueError("Invalid job status. Job status should be open and not pending")
            if process_steps[2].is_completed == False and status == JobStatus.OPEN:
                raise ValueError("Invalid job status. Job status should be pending and not open")
        return values
