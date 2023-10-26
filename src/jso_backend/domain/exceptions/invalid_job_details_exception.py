class InvalidJobDetailsError(Exception):
    def __init__(self, *args: object, message: str) -> None:
        super().__init__(*args)
        self.message = message
