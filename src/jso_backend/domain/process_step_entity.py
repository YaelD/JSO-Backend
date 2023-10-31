from pydantic import BaseModel, Field

from jso_backend.domain.step_type import StepType


class ProcessStepEntity(BaseModel, validate_assignment=True):
    name: str = Field(min_length=1, max_length=25)
    type: StepType = StepType.CUSTOM
    is_completed: bool = False

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, type(self)):
            return NotImplemented
        return self.name == __value.name and self.type == __value.type
