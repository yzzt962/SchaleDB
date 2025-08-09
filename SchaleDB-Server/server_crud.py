from sqlalchemy import *
from fastapi import *
engine = create_engine("sqlite:///./test.db", echo=True)
metadata = MetaData()
stutb = Table(
    'stutb',
    metadata,
    Column('id', Integer, primary_key=True,autoincrement=True),
    Column('name', String),
    Column('point',Integer)
)
metadata.create_all(engine)
def add(name:str, point:int):
    with engine.connect() as connection:
        res = connection.execute(insert(stutb).values(name=name,point=point))
        connection.commit()
        return "Success"
def list(formatted=False):
    with engine.connect() as connection:
        a = connection.execute(select(stutb))
        if formatted:
            return "\n".join(f"ID:{row.id}, Name:{row.name}, Point:{row.point}"for row in a)
        return [{"ID":row.id,"Name":row.name,"Point":row.point}for row in a]
def update_stu(id1:int,command:int,name:str,dp:int):
    with engine.begin() as connection:
        exist = connection.execute(select(stutb).where(stutb.c.id == id1)).first()
        if(not exist):
            raise HTTPException(status_code=404,detail="找不到这个学生")
        updt = {}
        if(command == 2):
            updt["name"] = name
        elif(command == 1):
            if (dp <= 0):
                raise HTTPException(status_code=400,detail="积分数量要大于0")
            updt["point"] = dp
        result = connection.execute(update(stutb).where(stutb.c.id == id1).values(**updt))
        if(result.rowcount == 0):
            raise HTTPException(status_code=500,detail="改动未生效")
        return {'status':"success","message":"改动陈公提交"}
def delete_student(id1:int):
    with engine.begin() as connection:
        cnt = connection.execute(select(stutb).where(stutb.c.id == id1)).first()
        if(not cnt):
            raise HTTPException(status_code=404,detail="找不到这个学生")
        result = connection.execute(stutb.delete().where(stutb.c.id == id1))
        afrow = result.rowcount
        return afrow
'''
def menu():
    while True:
        print("1.Add student")
        print("2.Change student info")
        print("3.List students' info")
        print("4.Delete student")
        print("5.Exit")
        cmd = input("Enter command:")
        if(cmd == "1"):
            print(add())
        elif(cmd == "2"):
            print(update())
        elif(cmd == "3"):
            print(list())
        elif(cmd == "4"):
            print(deletestu())
        elif (cmd == "5"):
            break
menu()
'''
