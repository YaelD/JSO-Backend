from datetime import datetime
from typing import Any

from sqlmodel import JSON, Column, Field, Relationship, SQLModel  # type:ignore

from jso_backend.domain.job_status_type import JobStatus


class DBJobModel(SQLModel, table=True):
    creation_date: datetime | None = datetime.now()
    company_name: str
    role: str
    status: JobStatus = JobStatus.PENDING
    job_link: str | None = None
    about: str | None = None
    tech_stack: list[str] = Field(sa_column=Column(JSON))
    id: int | None = Field(default=None, primary_key=True)
    process_steps: list[dict[str, Any]] = Field(sa_column=Column(JSON))
