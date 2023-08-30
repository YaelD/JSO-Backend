from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel  # type:ignore

if TYPE_CHECKING:
    from .attachment_model import Attachment
    from .interview_model import Interview
    from .job_info_model import JobInfo
    from .network_connection_model import NetworkConnection
    from .process_step_model import ProcessStep
    from .todo_model import Todo
    from .user_model import User


class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: datetime
    company_name: str
    role: str
    step: str
    status: StrEnum

    user_id: int = Field(default=None, foreign_key="user.id")
    user: "User" = Relationship(back_populates="jobs")
    job_info: "JobInfo" = Relationship(back_populates="job")
    process_steps: list["ProcessStep"] = Relationship(back_populates="job")
    interviews: list["Interview"] = Relationship(back_populates="job")
    attachments: list["Attachment"] = Relationship(back_populates="job")
    todos: list["Todo"] = Relationship(back_populates="job")
    network_connections: list["NetworkConnection"] = Relationship(back_populates="job")
