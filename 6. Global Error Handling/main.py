from fastapi import FastAPI, status, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

# Custom Global Exception Handler
class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={
        "success": False,
        "message": f"User {exc.name} not found" 
    })

@app.get("/user/{name}", status_code=status.HTTP_200_OK)
def get_user(name: str):
    if name != "Fahad":
        raise UserNotFoundException(name)
    return {
        "success": True,
        "name": name,
        "age": 27
    }


