from jso_backend.domain.job_process import JobProcess
from jso_backend.domain.process_step_entity import ProcessStepEntity
from jso_backend.models.process_step_model import DBProcessStepModel


class ProcessStepDBConverter:
    def convert_process_step_entity_to_db_process_step(
        self, process_step: ProcessStepEntity
    ) -> DBProcessStepModel:
        return DBProcessStepModel(
            name=process_step.name, type=process_step.type, is_completed=process_step.is_completed
        )

    def convert_process_step_list_to_db_process_step_list(
        self, job_process: JobProcess
    ) -> list[DBProcessStepModel]:
        db_process_steps: list[DBProcessStepModel] = []
        for i in range(0, len(job_process.process_steps)):
            converted_step: DBProcessStepModel = (
                self.convert_process_step_entity_to_db_process_step(job_process.process_steps[i])
            )
            converted_step.order = i
            db_process_steps.append(converted_step)
        return db_process_steps
