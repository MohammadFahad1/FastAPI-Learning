from fastapi import FastAPI

app = FastAPI()

@app.post("/create-user/")
def create_user(user: dict):
    return {
        "success": True,
        "message": "User created successfully",
        "user": user
    }

