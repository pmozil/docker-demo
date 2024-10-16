from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Create a simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Create another endpoint that takes a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Create a POST endpoint
@app.post("/create-item/")
def create_item(item: dict):
    return {"item": item, "message": "Item created successfully!"}
