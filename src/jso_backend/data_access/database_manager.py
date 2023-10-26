from sqlmodel import Session, SQLModel, create_engine


class DatabaseManager:
    _instance = None
    _password = "yd305110"
    _postgreSQL_url = f"postgresql://postgres:{_password}@localhost:5432/postgres"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        self.database_url = self._postgreSQL_url
        self.engine = create_engine(self.database_url, echo=True)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        return Session(self.engine)
