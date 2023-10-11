from abc import ABC, abstractmethod
from typing import Any

from jso_backend.domain.job_entity import JobEntity


class IJobDataAccess(ABC):
    @abstractmethod
    async def get_job_by_id(self, job_id: int) -> JobEntity:
        pass

    @abstractmethod
    async def get_list(self, limit: int = 0, offset: int = 0) -> list[JobEntity]:
        pass

    @abstractmethod
    async def create_job(self, job: JobEntity) -> JobEntity:
        pass

    @abstractmethod
    async def update_job(self, job_id: int, job_data: dict[str, Any]) -> JobEntity:
        pass

    @abstractmethod
    def delete_job(self, job_id: int) -> None:
        pass
