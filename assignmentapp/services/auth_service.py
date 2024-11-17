from assignmentapp.models.user import find_user_by_email
from assignmentapp.utils.jwt_handler import create_access_token
from passlib.hash import bcrypt

def authenticate_user(email: str, password: str):
    user = find_user_by_email(email)
    if user and bcrypt.verify(password, user["password"]):
        return user
    return None
