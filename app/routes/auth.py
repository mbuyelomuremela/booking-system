from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.users import UserData, UserRegisterData, UserLoginData
from app.database.database import get_db
from app.services.auth import create_user, get_user
from app.core.security import generate_access_token, get_current_user, verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserData)
def register_user(user_data: UserRegisterData, db: Session = Depends(get_db)):
    user = user_data.model_dump()
    return create_user(user,db)

@router.post("/login")
def login(userData: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user({"email": userData.username}, db)  
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"error": f"user with email {userData.username} does not exist"})
    if not verify_password(userData.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"error": "invalid email or password"})

    token = generate_access_token({"user_id": user.id})

    return {"access_token": token, "token_type": "Bearer"}
