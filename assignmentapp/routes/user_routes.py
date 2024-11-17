from fastapi import APIRouter, HTTPException, Depends
from assignmentapp.services.auth_service import create_access_token, authenticate_user
from assignmentapp.schemas.user_schema import UserRegister, UserLogin
from assignmentapp.models.user import create_user, find_user_by_email

user_router = APIRouter()

@user_router.post("/register")
def register_user(user: UserRegister):
    existing_user = find_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    create_user(user.dict())
    return {"message": "User registered successfully"}

@user_router.post("/login")
def login_user(user: UserLogin):
    user_data = authenticate_user(user.email, user.password)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
