from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel  # type:ignore

if TYPE_CHECKING:
    from .job_model import Job
    from .todo_model import Todo


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

    jobs: list["Job"] = Relationship(back_populates="user")
    todos: list["Todo"] = Relationship(back_populates="user")
