from uuid import UUID


class JobNotFoundError(Exception):
    def __init__(self, *args: object, id: UUID) -> None:
        super().__init__(*args)
        self.message = f"Job with id {id} not found"
