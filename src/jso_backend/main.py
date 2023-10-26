from fastapi import FastAPI

from jso_backend.api.routers import job_router
from jso_backend.data_access.database_manager import DatabaseManager

app = FastAPI()


app.include_router(job_router.router)


@app.on_event("startup")
def on_startup():
    db_manager = DatabaseManager()
    db_manager.create_db_and_tables()
