import uuid
from sqlalchemy import Column, String, Boolean, JSON
from sqlalchemy.dialects.postgresql import UUID
from ..core.database import Base

class Flow(Base):
    __tablename__ = "flows"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    trigger = Column(JSON)
    action = Column(JSON)
    enabled = Column(Boolean, default=True)