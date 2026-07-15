from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.service import Services
from app.schemas.service import ServiceAddModel

def get_services(db: Session):
    return db.query(Services).all()

def add_new_service(service: ServiceAddModel, db: Session):
    db_service = db.query(Services).filter(Services.name == service.name).first()
    if db_service:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Service with this name: {service.name} already exists."
        )
    new_service = Services(**service.model_dump())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service