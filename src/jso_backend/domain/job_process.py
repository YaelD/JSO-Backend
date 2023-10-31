from pydantic import BaseModel

from jso_backend.domain.process_step_entity import ProcessStepEntity
from jso_backend.domain.step_type import StepType

starting_steps: list[ProcessStepEntity] = [
    ProcessStepEntity(name=str(StepType.CONNECT), type=StepType.CONNECT),
    ProcessStepEntity(name=str(StepType.SEND_CV), type=StepType.SEND_CV),
    ProcessStepEntity(name=str(StepType.APPLIED), type=StepType.APPLIED),
]


class JobProcess(BaseModel, validate_assignment=True):
    steps_list: list[ProcessStepEntity] = starting_steps
