from typing import Any

from pydantic import BaseModel, Field, root_validator

from jso_backend.domain.step_type import StepType


class ProcessStepApiModel(BaseModel):
    name: str = Field(min_length=1, max_length=25)
    type: StepType = StepType.CUSTOM
    is_completed: bool = False

    @root_validator
    def validate_name_and_type(cls, values: dict[str, Any]) -> dict[str, Any]:
        name: str | None = values.get("name")
        type: StepType | None = values.get("type")
        if not name or not type:
            raise ValueError("Invalid process step. Process step must contain name and type")
        if type != StepType.CUSTOM and str(type) != name:
            raise ValueError(
                "Invalid process step. Name and type should be equals for non-custom process step type."
            )
        return values
