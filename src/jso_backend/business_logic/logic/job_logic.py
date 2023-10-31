from typing import Any

from jso_backend.domain.job_entity import JobEntity
from jso_backend.domain.job_status_type import JobStatus
from jso_backend.domain.process_step_entity import ProcessStepEntity


class JobLogic:
    def update_job_details(
        self,
        curr_job_in_db: JobEntity,
        job_details_to_update: dict[str, Any],
        process_steps: list[ProcessStepEntity] | None,
    ) -> None:
        if process_steps and job_details_to_update.get("status") is None:
            updated_status: JobStatus = self.update_job_status_by_process_step_list(
                process_steps=process_steps, curr_job_in_db=curr_job_in_db
            )
            job_details_to_update["status"] = updated_status

    def update_job_status_by_process_step_list(
        self, process_steps: list[ProcessStepEntity], curr_job_in_db: JobEntity
    ) -> JobStatus:
        if curr_job_in_db.status == JobStatus.PENDING and process_steps[2].is_completed:
            return JobStatus.OPEN
        elif curr_job_in_db.status == JobStatus.OPEN and not process_steps[2].is_completed:
            return JobStatus.PENDING
        return curr_job_in_db.status

    def generate_todos_according_the_current_process_step(self):
        pass
