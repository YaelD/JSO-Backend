from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel  # type:ignore

if TYPE_CHECKING:
    from .job_model import Job
    from .question_and_answer_model import QuestionAndAnswer


class Interview(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    interview_date: datetime
    title: str
    conclusions: str

    job_id: int = Field(default=None, foreign_key="job.id")
    job: "Job" = Relationship(back_populates="interviews")
    questions_and_answers: list["QuestionAndAnswer"] = Relationship(back_populates="interview")
