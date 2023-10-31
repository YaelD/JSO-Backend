import uuid
from datetime import date
from typing import Any

from pydantic import BaseModel, Field, root_validator, validator

from jso_backend.domain.job_status_type import JobStatus
from jso_backend.domain.process_step_entity import ProcessStepEntity
from jso_backend.domain.step_type import StepType

starting_steps: list[ProcessStepEntity] = [
    ProcessStepEntity(name=str(StepType.CONNECT), type=StepType.CONNECT),
    ProcessStepEntity(name=str(StepType.SEND_CV), type=StepType.SEND_CV),
    ProcessStepEntity(name=str(StepType.APPLIED), type=StepType.APPLIED),
]


class JobEntity(BaseModel, validate_assignment=True):
    company_name: str = Field(min_length=1, max_length=50)
    role: str = Field(min_length=1, max_length=50)
    id: uuid.UUID = uuid.uuid4()
    status: JobStatus = JobStatus.PENDING
    creation_date: date | None = date.today()
    job_link: str | None = ""
    about: str | None = ""
    tech_stack: list[str] = []
    process_steps: list[ProcessStepEntity] = starting_steps

    @validator("creation_date")
    @classmethod
    def validate_creation_date(cls, value: date) -> date:
        if value > date.today():
            raise ValueError("Invalid creation date. Creation date can not be a future date")
        return value

    @root_validator
    def validate_process_steps_and_status(cls, values: dict[str, Any]) -> dict[str, Any]:
        process_steps: list[ProcessStepEntity] | None = values.get("process_steps")
        status: JobStatus | None = values.get("status")
        if not process_steps or not status:
            raise ValueError("Invalid job entity. Job must contain process steps and status")
        if process_steps[2].is_completed == True and status == JobStatus.PENDING:
            raise ValueError("Invalid job status. Job status should be open and not pending")
        if process_steps[2].is_completed == False and status == JobStatus.OPEN:
            raise ValueError("Invalid job status. Job status should be pending and not open")
        return values
