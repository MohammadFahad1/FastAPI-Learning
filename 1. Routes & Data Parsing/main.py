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


# Query Parameters
# /products/?id=1
# /products/?id=2&name=abc
@app.get("/products/")
def get_product(id: int, name: str = None):
    return {
        "id": id,
        "product_name": name
    }

# With a default value
@app.get("/categories/")
def get_category(category_id: int, category_name: str = "General"):
    return {
        "category_id": category_id,
        "category_name": category_name
    }

@app.get("/items/")
def get_items(name: str = None, price: int = 0):
    return {
        "name": name,
        "price": price
    }
