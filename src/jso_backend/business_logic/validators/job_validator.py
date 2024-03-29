from typing import Any

from jso_backend.business_logic.validators.process_steps_validator import (
    ProcessStepsValidator,
)
from jso_backend.domain.exceptions.invalid_job_details_exception import (
    InvalidJobDetailsError,
)
from jso_backend.domain.job_entity import JobEntity
from jso_backend.domain.job_status_type import JobStatus
from jso_backend.domain.process_step_entity import ProcessStepEntity


class JobValidator:
    def __init__(
        self,
        job_entity: JobEntity,
        job_details_to_update: dict[Any, Any],
        process_steps: list[ProcessStepEntity] | None = None,
    ) -> None:
        self.job_entity = job_entity
        self.job_details_to_update = job_details_to_update
        self.process_steps = process_steps

    def validate_job_data_fields(
        self,
    ) -> None:
        self.validate_required_field_is_not_empty("company_name")
        self.validate_required_field_is_not_empty("role")
        if self.process_steps:
            if not ProcessStepsValidator().check_is_valid_process_step_list(
                process_step_list=self.process_steps
            ):
                raise InvalidJobDetailsError(message="Invalid process steps")
        status: JobStatus | None = self.job_details_to_update.get("status")
        if status and not self.validate_status(value=status):
            raise InvalidJobDetailsError(message="Invalid status type")

    def validate_required_field_is_not_empty(self, field: str):
        required_field: str | None = self.job_details_to_update.get(field)
        if required_field is not None and required_field == "":
            raise InvalidJobDetailsError(message=f"Invalid {field}. {field} can not be empty")

    def validate_status(self, value: JobStatus) -> bool:
        match value:
            case JobStatus.CLOSE:
                return True

            case JobStatus.OPEN:
                if self.process_steps:
                    return True if self.process_steps[2].is_completed else False
                else:
                    return True if self.job_entity.process_steps[2].is_completed else False

            case JobStatus.PENDING:
                if self.process_steps:
                    return True if not self.process_steps[2].is_completed else False
                else:
                    return True if self.job_entity.status == JobStatus.PENDING else False
