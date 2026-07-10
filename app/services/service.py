from sqlalchemy.orm import Session

from app.models.service import Services
from app.schemas.service import ServiceAddModel

def get_services(db: Session):
    return db.query(Services).all()

def add_new_service(service: ServiceAddModel, db: Session):
    pass