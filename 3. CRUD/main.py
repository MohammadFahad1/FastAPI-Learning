from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool


@app.post('/todos/')
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "success": True,
        "message": "Todo created successfully",
        "todo": todo
    }

@app.get('/todos/')
def get_todos():
    return todos

@app.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    todo = next(filter(lambda x: x.id == todo_id, todos), None)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo

@app.put('/todos/{todo_id}/')
def update_todo(todo_id: int, updated_todo: Todo):
    todo = next(filter(lambda x: x.id == todo_id, todos), None)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    todo.title = updated_todo.title
    todo.completed = updated_todo.completed
    return {
        "success": True,
        "message": "Todo updated successfully",
        "todo": todo
    }

@app.delete('/todos/{todo_id}/')
def delete_todo(todo_id: int):
    todo = next(filter(lambda x: x.id == todo_id, todos), None)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    todos.remove(todo)
    return {
        "success": True,
        "message": "Todo deleted successfully",
        "todo": todo
    }
