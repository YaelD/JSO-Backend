from typing import Any

from jso_backend.domain.job_entity import JobEntity
from jso_backend.domain.job_process import JobProcess
from jso_backend.domain.job_status_type import JobStatus


class JobLogic:
    def update_job_details(
        self,
        curr_job_in_db: JobEntity,
        job_details_to_update: dict[str, Any],
        job_process: JobProcess | None,
    ) -> None:
        if job_process and job_details_to_update.get("status") is None:
            updated_status: JobStatus = self.update_job_status_by_process_step_list(
                job_process=job_process, curr_job_in_db=curr_job_in_db
            )
            job_details_to_update["status"] = updated_status

    def update_job_status_by_process_step_list(
        self, job_process: JobProcess, curr_job_in_db: JobEntity
    ) -> JobStatus:
        if curr_job_in_db.status == JobStatus.PENDING and job_process.steps_list[2].is_completed:
            return JobStatus.OPEN
        elif (
            curr_job_in_db.status == JobStatus.OPEN and not job_process.steps_list[2].is_completed
        ):
            return JobStatus.PENDING
        return curr_job_in_db.status

    def generate_todos_according_the_current_process_step(self):
        pass
