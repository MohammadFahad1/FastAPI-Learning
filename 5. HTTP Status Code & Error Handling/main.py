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

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {
        "name": "Fahad",
        "age": 27,
        "message": "User fetched successfully"
    }

