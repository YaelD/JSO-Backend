from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel  # type:ignore

from jso_backend.domain.step_type import StepType

if TYPE_CHECKING:
    from .job_model import DBJobModel


class DBProcessStepModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    type: StepType = StepType.CUSTOM
    is_completed: bool = False
    order: int = 2

    job_id: int = Field(default=None, foreign_key="dbjobmodel.id")
    job: "DBJobModel" = Relationship(back_populates="process_steps")
