from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel  # type:ignore

if TYPE_CHECKING:
    from .job_model import Job


class JobInfo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_link: str
    about: str
    tech_stack: list[str]

    job_id: int = Field(default=None, foreign_key="job.id")
    job: "Job" = Relationship(sa_relationship_kwargs={"uselist": False}, back_populates="job_info")
