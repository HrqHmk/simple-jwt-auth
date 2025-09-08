from sqlalchemy import Column, String, BIGINT, ForeignKey, DateTime, func
from src.models.sqlite.settings.base import Base

class OrderTable(Base):
    __tablename__ = "orders"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    product = Column(String)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    user_id = Column(BIGINT, ForeignKey("users.id"))

    def __repr__(self):
        return f"Order [username={self.username}, product={self.product}]"
