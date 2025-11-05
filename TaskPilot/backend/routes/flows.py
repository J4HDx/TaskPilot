from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from .. import models, schemas
from ..core.database import SessionLocal

router = APIRouter()

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/flows", response_model=schemas.Flow, status_code=status.HTTP_201_CREATED)
def create_flow(flow: schemas.FlowCreate, db: Session = Depends(get_db)):
    db_flow = models.Flow(**flow.model_dump())
    db.add(db_flow)
    db.commit()
    db.refresh(db_flow)
    return db_flow

@router.get("/flows", response_model=List[schemas.Flow])
def get_flows(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    flows = db.query(models.Flow).offset(skip).limit(limit).all()
    return flows

@router.get("/flows/{flow_id}", response_model=schemas.Flow)
def get_flow(flow_id: str, db: Session = Depends(get_db)):
    db_flow = db.query(models.Flow).filter(models.Flow.id == flow_id).first()
    if db_flow is None:
        raise HTTPException(status_code=404, detail="Flow not found")
    return db_flow

@router.put("/flows/{flow_id}", response_model=schemas.Flow)
def update_flow(flow_id: str, flow: schemas.FlowCreate, db: Session = Depends(get_db)):
    db_flow = db.query(models.Flow).filter(models.Flow.id == flow_id).first()
    if db_flow is None:
        raise HTTPException(status_code=404, detail="Flow not found")

    for var, value in vars(flow).items():
        setattr(db_flow, var, value) if value else None

    db.add(db_flow)
    db.commit()
    db.refresh(db_flow)
    return db_flow

@router.delete("/flows/{flow_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_flow(flow_id: str, db: Session = Depends(get_db)):
    db_flow = db.query(models.Flow).filter(models.Flow.id == flow_id).first()
    if db_flow is None:
        raise HTTPException(status_code=404, detail="Flow not found")
    db.delete(db_flow)
    db.commit()
    return