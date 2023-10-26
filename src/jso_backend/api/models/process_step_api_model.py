from pydantic import BaseModel

from jso_backend.domain.step_type import StepType


class ProcessStepApiModel(BaseModel):
    name: str
    type: StepType = StepType.CUSTOM
    is_completed: bool = False
