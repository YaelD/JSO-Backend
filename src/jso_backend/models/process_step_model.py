from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel  # type:ignore

if TYPE_CHECKING:
    from .job_model import Job


class ProcessStep(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    step: str
    is_completed_step: bool = Field(default=False)

    job_id: int = Field(default=None, foreign_key="job.id")
    job: "Job" = Relationship(back_populates="process_steps")
