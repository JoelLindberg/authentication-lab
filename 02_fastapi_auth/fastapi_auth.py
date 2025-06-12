from fastapi import FastAPI, Depends, HTTPException, Header
from argon2 import PasswordHasher
import logging


app = FastAPI()
logger = logging.getLogger("uvicorn")

# Simulated token for demonstration
ph = PasswordHasher()
HASHED_TOKEN = ph.hash("supersecrettoken") # Should be in a DB but we won't do this in this demo.


def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    
    token = authorization.split("Bearer ")[-1]
    if ph.verify(HASHED_TOKEN, "supersecrettoken") != True:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    logger.info(f"Rehashing needed: {ph.check_needs_rehash(HASHED_TOKEN)}") # Apparently it's best practice to check, and if necessary rehash passwords after each successful authentication. We don't do this in this demo.

    return token

@app.get("/secure-data")
def secure_endpoint(token: str = Depends(verify_token)):
    return {"message": "You have access!", "token": token}


'''
# Simulated token for demonstration
VALID_TOKEN = "supersecrettoken"

def verify_token(token: str = Header(None)):
    if not token or token != VALID_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/secure-data")
def secure_endpoint(token: str = Depends(verify_token)):
    return {"message": "You have access!", "token": token}
'''