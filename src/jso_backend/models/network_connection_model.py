from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel  # type:ignore

if TYPE_CHECKING:
    from .job_model import Job


class NetworkConnection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    role: str
    linkedin_link: str
    send_cv: bool
    applied: bool = Field(default=None)

    job_id: int = Field(default=None, foreign_key="job.id")
    job: "Job" = Relationship(back_populates="network_connections")
