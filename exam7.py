from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/html1")
async def test1(request: Request):
    return templates.TemplateResponse(request, "exam7_1.html")

@app.get("/html2") 
async def test2(request: Request):
    return templates.TemplateResponse(request, "exam7_2.html")


