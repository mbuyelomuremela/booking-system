from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import Users
from app.core.security import hash_password

# create new user account
def create_user(userData: dict, db: Session):
    user = db.query(Users).filter(Users.email == userData["email"]).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"error": "error", "message": f"email {userData["email"]} is already taken"})
    
    user_copy = userData.copy()
    print(user_copy)
    user_copy.update({"hashed_password": f"{hash_password(user_copy["password"])}"})

    del user_copy["password"]

    new_user = Users(**user_copy)
    db.add(new_user)
    db.commit()
    db.flush(new_user)
    return new_user

def get_user(userData: dict, db: Session):
    return db.query(Users).filter(Users.email == userData["email"]).first()
    