from jso_backend.domain.job_process import JobProcess, starting_steps
from jso_backend.domain.step_type import StepType


class ProcessStepsValidator:
    def check_is_valid_process_step_list(self, job_process: JobProcess) -> bool:
        if len(job_process.steps_list) < 3:
            return False
        else:
            if job_process.steps_list[0:3] != starting_steps:
                return False
            for index, step in enumerate(job_process.steps_list):
                if step.is_completed == False:
                    if not all(
                        process_step.is_completed == False
                        for process_step in job_process.steps_list[index:]
                    ):
                        return False
                    break
            for step in job_process.steps_list:
                if step.type != StepType.CUSTOM and step.name != str(step.type):
                    return False
        return True
