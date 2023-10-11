from jso_backend.domain.process_step_entity import ProcessStepEntity
from jso_backend.domain.step_type import StepType

starting_steps: list[ProcessStepEntity] = [
    ProcessStepEntity(StepType.CONNECT, StepType.CONNECT),
    ProcessStepEntity(StepType.SEND_CV, StepType.SEND_CV),
    ProcessStepEntity(StepType.APPLIED, StepType.APPLIED),
]


class JobProcess:
    def __init__(self, steps_list: list[ProcessStepEntity] = starting_steps) -> None:
        self.process_steps: list[ProcessStepEntity] = steps_list
        self.curr_step: ProcessStepEntity = starting_steps[0]
        self.curr_step_order: int = 0

    def add_process_step(self, new_process_step: ProcessStepEntity):
        self.process_steps.append(new_process_step)
