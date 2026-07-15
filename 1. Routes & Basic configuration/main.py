from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello World"
    }

# run using: uvicorn main:app --reload

@app.get("/about")
def about():
    return {
        "message": "About Page"
    }

@app.get("/users")
def users():
    return {
        "users": ["Fahad", "Monshi"]
    }


# -----------------------------------------------------
# Dynamic Routing
# -----------------------------------------------------

# Path Parameters
# /users/1/
# /users/2/
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }

@app.get('/users/{user_name}/')
def get_user(user_name: str):
    return {
        "user_name": user_name
    }
