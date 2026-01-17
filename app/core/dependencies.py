# Dependency injection logic fior Api key and JWT token validation
from fastapi import Header, HTTPException, Security
from app.core.config import settings
from app.core.security import verify_token


def get_api_key(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="INVALID API key")


def get_current_user(token: str = Header(...)):
    payload = verify_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid JWT token.")
    return payload
