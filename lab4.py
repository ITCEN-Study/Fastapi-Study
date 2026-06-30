from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# css, 이미지 마운트
app.mount("/static", StaticFiles(directory="static"), name="static")

# 진자2
templates = Jinja2Templates(directory="templates")

@app.get("/lab4",  response_class=HTMLResponse)
async def lab4_main(request: Request):
    return templates.TemplateResponse(request, "lab4_1.html")

@app.get("/lab4/{name}",  response_class=HTMLResponse)
async def lab4_detail(request: Request, name: str):
    # 이미지 매핑
    if name == "둘리":
        img_name = "dooly.jpg"
    elif name == "도우너":
        img_name = "dauner.png"
    else:
        img_name = "ddochi.jpg"
    
    return templates.TemplateResponse(
        request,
        "lab4_2.html",
        {"name": name, "img_name": img_name}
    )