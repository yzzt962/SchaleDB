from fastapi import *
from server_crud import add,delete_student,update_stu
from server_crud import list
from server_crud import engine
from sqlalchemy import text
from typing import *
app = FastAPI(title="Schale DB API",version="0.1.0",description="基于FastAPI的学生管理系统API")
@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post('/create/{name}/{point}')
async def create(name: str, point: int):
    add(name, point)
    return {
        'status':"success",
        'message':f"已经创建学生{name}！",
        'data':{"name": name, "point": point}
    }
@app.delete('/delete/{id1}')
async def delete_route(id1: int):
    return {
        'status':"success",
        'message':delete_student(id1)
    }

@app.put('/update/{id}/{command}/{name}/{dp}')
async def update_route(id: int, command: int, name: str, dp: int):
    return {
        'status':"success",
        'message':update_stu(id, command, name, dp),
    }
@app.get('/list')
async def list_route():
    with engine.connect() as conn:
        students = list()
        return {
            'status':"success",
            'message':"遍历完成！",
            'students':students
        }
@app.get('/student/{id}')
async def student_route(id: int):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM stutb WHERE id = :id"),{"id":id}).fetchone()
        if not result:
            raise HTTPException(status_code=404,detail="student not found")
        return {'status':"success","data":result._asdict()}