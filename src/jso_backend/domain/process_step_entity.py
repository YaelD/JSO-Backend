from jso_backend.domain.step_type import StepType


class ProcessStepEntity:
    def __init__(self, name: str, type: StepType = StepType.CUSTOM, is_completed: bool = False):
        self.name = name
        self.type = type
        self.is_completed = is_completed
