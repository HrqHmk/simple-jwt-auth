from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class UserTable(Base):
    __tablename__ = "users"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"User [username={self.username}]"
