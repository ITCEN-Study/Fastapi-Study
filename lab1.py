# 1
from fastapi import FastAPI

app = FastAPI()

@app.get("/lab1/{name}/{pgm}")
async def read_item(name : str, pgm : str):
 return {"name": name, "pgm" : pgm}