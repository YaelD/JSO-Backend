from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import JSON, Column, Field, Relationship, SQLModel  # type:ignore

from jso_backend.common.job_status_type import JobStatus

if TYPE_CHECKING:
    from .process_step_model import DBProcessStepModel


class DBJobModel(SQLModel, table=True):
    creation_date: datetime | None = datetime.now()
    company_name: str
    role: str
    status: JobStatus = JobStatus.PENDING
    job_link: str | None = None
    about: str | None = None
    tech_stack: list[str] = Field(sa_column=Column(JSON))
    id: int | None = Field(default=None, primary_key=True)
    curr_step_id: int | None

    process_steps: list["DBProcessStepModel"] = Relationship(back_populates="job")
