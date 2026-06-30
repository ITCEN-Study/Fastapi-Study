# 3
from fastapi import FastAPI

app = FastAPI()

@app.get("/lab3/{format}/{item}")
def read_lab3(format: str, item: str, page: int | None = None):
    # page 값 전달 여부 -> 출력 문자열
    page_str = f"{page} 페이지" if page is not None else "모든 페이지"

    result_message = f"{item} 에 대한 자료를 {format} 형식으로 {page_str}를 요청했어요."
    
    return {"result": result_message}