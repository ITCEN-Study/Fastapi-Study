from typing import Dict, Annotated
from fastapi import FastAPI, Form
from transformers import pipeline
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
classifier = None

@asynccontextmanager
async def startup(app: FastAPI):
    global classifier 
    classifier = pipeline("sentiment-analysis")
    print("Model Loaded:", classifier)
    yield

app = FastAPI(lifespan=startup)
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.post("/predict", response_model=Dict)
def predict(content: Annotated[str, Form()]):
    result = classifier(content)
    sentiment = result[0]['label']

    if sentiment == "POSITIVE":
        img = "/static/images/positive.png"
    else:
        img = "/static/images/negative.png"

    return HTMLResponse(content=f"""
        <html>
        <head>
        <meta charset="UTF-8">
        <title>Sentiment Analysis Result</title>
        </head>
        <body>
        <img src="{img}" width="200px">
        <br>
        </body>
        </html>
    """)

@app.get("/")
async def main():
    content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Hugging Face AI Model FastAPI 활용 실습</title>
        <style>
            .eva {
                width: 300px;
                height: 30px;
                font-size: 16px;
            }
        </style>
    </head>
    <body>
        <h1>Hugging Face AI Model FastAPI 활용 실습</h1>
        <hr>
        <h2>긍정 & 부정을 체크하려는 문장을 입력하세요</h2>
        <hr>
        <form action="/predict" method="post">
            <input class="eva" name="content" type="text" placeholder="분석을 원하는 글을 입력하세요"><br><br>
            <input type="submit" value="요청">
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=content)
