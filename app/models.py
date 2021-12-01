from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    description = Column(String, nullable=False)
    is_completed = Column(Boolean, nullable=False, server_default='FALSE')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
