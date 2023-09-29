from jso_backend.business_logic.process_step import ProcessStep
from jso_backend.common.step_type import StepType
from jso_backend.models.job_model import DBJobModel
from jso_backend.models.process_step_model import DBProcessStepModel

starting_steps: list[ProcessStep] = [
    ProcessStep(StepType.CONNECT, StepType.CONNECT),
    ProcessStep(StepType.SEND_CV, StepType.SEND_CV),
    ProcessStep(StepType.APPLIED, StepType.APPLIED),
]


class JobProcess:
    def __init__(self, steps_list: list[ProcessStep] = starting_steps) -> None:
        self.process_steps: list[ProcessStep] = steps_list

    def add_process_step(self, new_process_step: ProcessStep):
        self.process_steps.append(new_process_step)

    def convert_process_steps_to_DBProcessSteps(self, job: DBJobModel) -> list[DBProcessStepModel]:
        list_db_process_steps: list[DBProcessStepModel] = []
        for index in range(len(self.process_steps)):
            list_db_process_steps.append(
                self.process_steps[index].convert_process_step_to_DBProcessStep(
                    order=index, job=job
                )
            )
        return list_db_process_steps
