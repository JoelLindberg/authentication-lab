from fastapi import FastAPI, Depends, HTTPException, Header


app = FastAPI()

# Simulated token for demonstration
VALID_TOKEN = "supersecrettoken"

def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    
    token = authorization.split("Bearer ")[-1]
    if token != VALID_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
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