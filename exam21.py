from fastapi import FastAPI, HTTPException
from openai import OpenAI

app = FastAPI()
openai_client = OpenAI(api_key="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")

@app.get("/chat")
async def ask_question(q : str):   
    try:
        response = openai_client.responses.create(
            model="gpt-4o-mini",
            instructions="당신은 브라우저 사용자에게 명확한 정보를 전달하는 유능한 웹 비서입니다.", 
            input=q,  
            temperature=0.7
        )       
        return {"answer": response.output_text, "status": "success"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API 처리 오류: {str(e)}") 