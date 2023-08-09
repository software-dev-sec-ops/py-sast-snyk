from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/items")
def read():
    return {"Hello": "World"}


@app.get("/items/{id}")
def read_item(id: int, q: Optional[str] = None):
    return {"id": id, "q": q}


@app.put("/items/{id}")
def read_item(id: int):
    return {"id": id}


# if __name__ == "__main__":
#     uvicorn.run("main:app", port=8000, log_level="info")