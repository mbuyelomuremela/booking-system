from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.user import get_user_by_id 
from app.core.security import get_current_user
from app.schemas.users import UserData

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me", response_model=UserData)
def get_user(id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_user_by_id(id,db)


