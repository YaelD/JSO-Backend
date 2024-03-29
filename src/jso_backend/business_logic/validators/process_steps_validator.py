from jso_backend.domain.job_entity import starting_steps
from jso_backend.domain.process_step_entity import ProcessStepEntity
from jso_backend.domain.step_type import StepType


class ProcessStepsValidator:
    def check_is_valid_process_step_list(self, process_step_list: list[ProcessStepEntity]) -> bool:
        if len(process_step_list) < 3:
            return False
        else:
            if process_step_list[0:3] != starting_steps:
                return False
            for index, step in enumerate(process_step_list):
                if step.is_completed == False:
                    if not all(
                        process_step.is_completed == False
                        for process_step in process_step_list[index:]
                    ):
                        return False
                    break
            for step in process_step_list:
                if step.type != StepType.CUSTOM and step.name != str(step.type):
                    return False
        return True
