from typing import Any

from jso_backend.domain.process_step_entity import ProcessStepEntity


class ProcessStepDBConverter:
    def convert_list_of_process_step_entity_to_list_of_dict(
        self, process_steps: list[ProcessStepEntity]
    ) -> list[dict[str, Any]]:
        dict_process_steps: list[dict[str, Any]] = []
        for step in process_steps:
            dict_process_steps.append(step.dict())
        return dict_process_steps

    def convert_list_of_dicts_to_process_step_entity_list(
        self, dict_process_steps: list[dict[str, Any]]
    ) -> list[ProcessStepEntity]:
        process_step_entity_list: list[ProcessStepEntity] = []
        for dict_step in dict_process_steps:
            process_step_entity_list.append(ProcessStepEntity(**dict_step))
        return process_step_entity_list
