from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    score: int
    food: str | None = None

# 학생 인스턴스를 저장할 리스트
students_list = []

@app.post("/students", status_code=201)
async def create_student(student: Student):
    students_list.append(student)
    return student

@app.get("/students")
async def get_students():
    return students_list
