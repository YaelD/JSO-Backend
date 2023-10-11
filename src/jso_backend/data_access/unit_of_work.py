from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from jso_backend.data_access.database_manager import DatabaseManager


class UnitOfWork:
    @asynccontextmanager
    async def create(self) -> AsyncGenerator[Any, Any]:
        with DatabaseManager().get_session() as session:
            yield session
