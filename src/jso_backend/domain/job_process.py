from jso_backend.domain.process_step_entity import ProcessStepEntity
from jso_backend.domain.step_type import StepType

starting_steps: list[ProcessStepEntity] = [
    ProcessStepEntity(str(StepType.CONNECT), StepType.CONNECT),
    ProcessStepEntity(str(StepType.SEND_CV), StepType.SEND_CV),
    ProcessStepEntity(str(StepType.APPLIED), StepType.APPLIED),
]


class JobProcess:
    def __init__(self, steps_list: list[ProcessStepEntity] = starting_steps) -> None:
        self.process_steps: list[ProcessStepEntity] = steps_list
