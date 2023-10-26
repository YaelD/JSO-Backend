from typing import Any

from jso_backend.domain.step_type import StepType


class ProcessStepEntity:
    def __init__(
        self,
        name: str,
        type: StepType = StepType.CUSTOM,
        is_completed: bool = False,
    ):
        self.name = name
        self.type = type
        self.is_completed = is_completed

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "is_completed": self.is_completed,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        return cls(
            name=data.get("name", ""),
            type=data.get("type", StepType.CUSTOM),
            is_completed=data.get("is_completed", False),
        )

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, type(self)):
            return NotImplemented
        return self.name == __value.name and self.type == __value.type
