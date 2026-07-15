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
