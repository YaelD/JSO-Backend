from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel  # type:ignore

if TYPE_CHECKING:
    from .job_model import Job
    from .user_model import User


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task: str
    isCompletedTask: bool
    isNotified: bool
    scheduleTime: datetime = Field(default=None, index=True)

    job_id: int = Field(default=None, foreign_key="job.id")
    job: "Job" = Relationship(back_populates="todos")
    user_id: int = Field(default=None, foreign_key="user.id")
    user: "User" = Relationship(back_populates="todos")
