from sqlalchemy import Column, String, BIGINT, ForeignKey
from src.models.sqlite.settings.base import Base

class OrderTable(Base):
    __tablename__ = "orders"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    product = Column(String)
    description = Column(String)
    order_date = Column()
    user_id = Column(BIGINT, ForeignKey("users.id"))

    def __repr__(self):
        return f"Order [username={self.username}, product={self.product}]"
