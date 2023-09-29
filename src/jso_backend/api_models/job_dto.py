from datetime import datetime

from pydantic import BaseModel

from jso_backend.common.job_status_type import JobStatus


class JobReceive(BaseModel):
    creation_date: datetime | None = datetime.now()
    company_name: str
    role: str
    status: JobStatus = JobStatus.PENDING
    job_link: str | None = None
    about: str | None = None
    tech_stack: list[str] = []


class JobSend(JobReceive):
    id: int
    # curr_step_id: int = 0
    curr_step_name: str = ""


class JobUpdate(BaseModel):
    creation_date: datetime | None = None
    company_name: str | None = None
    role: str | None = None
    status: JobStatus | None = None
    job_link: str | None = None
    about: str | None = None
    tech_stack: list[str] | None = None
