from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

@app.post("/create_user/", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User created successfully",
        "data": {
            "name": "Fahad",
            "age": 27
        }
    }

@app.get("/user/", status_code=status.HTTP_200_OK)
def get_user():
    return {
        "name": "Fahad",
        "age": 27,
        "message": "User fetched successfully"
    }

