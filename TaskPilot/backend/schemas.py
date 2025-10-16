import uuid
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class Trigger(BaseModel):
    connector: str
    event: str
    config: Dict[str, Any] = {}

class Action(BaseModel):
    connector: str
    action: str
    config: Dict[str, Any] = {}

class FlowBase(BaseModel):
    name: str
    description: Optional[str] = None
    trigger: Trigger
    action: Action
    enabled: bool = True

class FlowCreate(FlowBase):
    pass

class Flow(FlowBase):
    id: str

    class Config:
        from_attributes = True