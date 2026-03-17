from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running"}
@app.get("/user/{username}")
def get_user(username: str):
    return {"user": username}
@app.get("/search")
def search(q: str, limit: int = 10):
    return {
        "query": q,
        "limit": limit
    }
from pydantic import BaseModel

class AddInput(BaseModel):
    a: int
    b: int

@app.post("/add")
def add(data: AddInput):
    return {"sum": data.a + data.b}
@app.put("/user/{id}")
def update_user(id: int, name: str):
    return {"id": id, "name": name}
@app.delete("/user/{id}")
def delete_user(id: int):
    return {"deleted": id}
