from jso_backend.api.models.process_step_api_model import ProcessStepApiModel
from jso_backend.domain.job_process import JobProcess
from jso_backend.domain.process_step_entity import ProcessStepEntity


class ProcessStepConverter:
    def convert_dict_process_step_list_to_job_process(
        self, dict_process_steps: list[ProcessStepApiModel]
    ) -> JobProcess:
        process_step_entity_list: list[ProcessStepEntity] = []
        for step in dict_process_steps:
            process_step_entity_list.append(ProcessStepEntity(**step.dict()))
        return JobProcess(steps_list=process_step_entity_list)

    def convert_process_step_entity_to_process_step_api(
        self, process_step_entity_list: list[ProcessStepEntity]
    ) -> list[ProcessStepApiModel]:
        return [
            ProcessStepApiModel(name=step.name, type=step.type, is_completed=step.is_completed)
            for step in process_step_entity_list
        ]
