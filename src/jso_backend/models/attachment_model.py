from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel  # type:ignore

if TYPE_CHECKING:
    from .job_model import Job


class Attachment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    file_path: str
    file_name: str
    file_data: bytes

    job_id: int = Field(default=None, foreign_key="job.id")
    job: "Job" = Relationship(back_populates="attachments")
