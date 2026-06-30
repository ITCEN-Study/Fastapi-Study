from fastapi import FastAPI

app = FastAPI()

@app.get("/lab2")
async def read_item_query(
    name: str = "고길동", 
    color: str = "핑크색", 
    age: int = 50
):
    return {
        "name": name, 
        "color": color, 
        "age": age
    }