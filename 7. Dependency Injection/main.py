from fastapi import FastAPI, status, HTTPException, Request, Depends, Header
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

def verify_token(token: str = Header(None)):
    if token != "secret_token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return {
        "success": True,
        "message": "Token verified successfully",
        "user": {
            "name": "Fahad",
            "age": 27
        }
    }

@app.get("/secure-data/", status_code=status.HTTP_200_OK)
def secure_data(user = Depends(verify_token)):
    return {
        "success": True,
        "message": "Secure data fetched successfully",
        "user": user
    }


# def common_logic():
#     return {
#         "message": "Common logic executed successfully"
#     }

# @app.get("/home/")
# def home(data = Depends(common_logic)):
#     return data

"""
def get_current_user():
    return {
        "name": "Fahad",
        "age": 27
    }

@app.get("/profile/", status_code=status.HTTP_200_OK)
def profile(user = Depends(get_current_user)):
    return user

@app.get("/dashboard/", status_code=status.HTTP_200_OK)
def dashboard(user = Depends(get_current_user)):
    return user
"""

