# FastAPI Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Creating web API with FastAPI](#creating-web-api-with-fastapi)
- [CORS settings](#cors-settings)

## Creating web API with FastAPI
1. Install package for FastAPI, and an ASGI server (Uvicorn).
```
$ pip install fastapi uvicorn[standard]
```

2. Create application.
```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello World!"}

if __name__ == '__main__':
    uvicorn.run("main:app")
```

- Parameters can be taken from the path. `item_id` is the path parameter, and `q` is an option query parameter, and must follow the type.
```python
@app.get("/items/{item_id}")
def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

- Request body is accepted by declaring the body as a class of `BaseModel` from `Pydantic`.
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = False

@app.post("/items/{item_id}")
def post_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}
```

## CORS settings
1. Configure `CORSMiddleware` for the FastAPI application. Use `*` as a wild card.
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
```
