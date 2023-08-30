from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel  # type:ignore

if TYPE_CHECKING:
    from .interview_model import Interview


class QuestionAndAnswer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question: str
    answer: str

    interview_id: int = Field(default=None, foreign_key="interview.id")
    interview: "Interview" = Relationship(back_populates="questions_and_answers")
