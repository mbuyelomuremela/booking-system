from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.schemas.service import ServiceData, ServiceAddModel
from app.services.service import get_services as get_all_services, add_new_service
from app.core.security import get_current_user

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)


@router.get("/", response_model=List[ServiceData])
def get_services(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return get_all_services(db)

@router.post("/add")
def add_service( service_data: ServiceAddModel ,db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return add_new_service(service_data, db)