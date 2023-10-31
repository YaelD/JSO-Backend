import uuid
from datetime import date
from typing import Any

from sqlmodel import JSON, Column, Field, Relationship, SQLModel  # type:ignore

from jso_backend.domain.job_status_type import JobStatus


class DBJobModel(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    creation_date: date | None = date.today()
    company_name: str
    role: str
    status: JobStatus = JobStatus.PENDING
    job_link: str | None = None
    about: str | None = None
    tech_stack: list[str] = Field(sa_column=Column(JSON))
    process_steps: list[dict[str, Any]] = Field(sa_column=Column(JSON))
