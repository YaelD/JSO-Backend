from enum import StrEnum


class JobStatus(StrEnum):
    PENDING = "pending"
    OPEN = "open"
    CLOSE = "close"
