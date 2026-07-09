from sqlalchemy.orm import Session

from app.models.user import Users

def get_user_by_id(id:int, db:Session):
    return db.query(Users).filter(Users.id == id).first()