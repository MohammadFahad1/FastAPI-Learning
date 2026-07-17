from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    name: str
    age: int

@app.get("/users/", response_model=UserResponse)
def get_user():
    return {
        "name": "Fahad",
        "age": 27,
        "password": "123456"
    }

