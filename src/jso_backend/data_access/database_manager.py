from sqlmodel import Session, SQLModel, create_engine


class DatabaseManager:
    _instance = None
    _sqlite_file_name = "database.db"
    _sqlite_url = f"sqlite:///{_sqlite_file_name}"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        self.database_url = self._sqlite_url
        connect_args = {"check_same_thread": False}
        self.engine = create_engine(self.database_url, echo=True, connect_args=connect_args)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        return Session(self.engine)
