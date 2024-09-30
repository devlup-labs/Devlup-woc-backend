from datetime import datetime, timedelta
from typing import List
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from grpc import Status
from jose import JWTError
import jwt
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3600
load_dotenv()  
import os
SECRET_KEY = os.environ.get("SECRET_KEY")
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def get_current_user_role(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_role = payload.get("role")
        if user_role is None:
            raise HTTPException(
                status_code=Status.HTTP_401_UNAUTHORIZED,
                detail="Role not found in token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user_role
    except JWTError:
        raise HTTPException(
            status_code=Status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

def role_required(required_roles: List[str]):
    def role_dependency(user_role: str = Depends(get_current_user_role)):
        
        if user_role not in required_roles:
            raise HTTPException(
                status_code=Status.HTTP_403_FORBIDDEN,
                detail=f"Insufficient permissions. Required roles: {required_roles}",
            )
        return user_role
    return role_dependency

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        role = payload.get("role")
        if user_id is None or role is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token, user_id or role missing",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return {"id": user_id, "role": role}
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )