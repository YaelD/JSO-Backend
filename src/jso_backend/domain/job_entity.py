from datetime import datetime

from jso_backend.domain.job_process import JobProcess
from jso_backend.domain.job_status_type import JobStatus


class JobEntity:
    def __init__(
        self,
        company_name: str,
        role: str,
        id: int | None = None,
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
        self.id = id
        self.status = status
        self.job_link = job_link
        self.about = about
        self.tech_stack = tech_stack
        self.process_steps = process_steps
        self.curr_step = self.process_steps.curr_step.name
