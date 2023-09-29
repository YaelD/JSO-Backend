from jso_backend.common.step_type import StepType
from jso_backend.models.job_model import DBJobModel
from jso_backend.models.process_step_model import DBProcessStepModel


class ProcessStep:
    def __init__(self, name: str, type: StepType = StepType.CUSTOM, is_completed: bool = False):
        self.name = name
        self.type = type
        self.is_completed = is_completed

    def convert_process_step_to_DBProcessStep(
        self, order: int, job: DBJobModel
    ) -> DBProcessStepModel:
        return DBProcessStepModel(
            name=self.name, type=self.type, is_completed=self.is_completed, order=order, job=job
        )
