from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
# from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# 创建 FastAPI 应用
app = FastAPI()

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 允许的前端地址
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)
# 依赖函数：获取数据库会话
def get_db():
  db = SessionLocal() # 创建会话
  try:
    yield db
  finally:
    db.close() # 关闭会话

# 获取学习来源数据
@app.get('/api/getSourceList') #response_model=list[schemas.Task] 这个干嘛的
def find_sources(db: Session = Depends(get_db)):
  sources = crud.querySourceList(db)
  return {'data':sources,'code': 200}

# 获取所有单词
@app.get('/api/getAllWords') #response_model 这个干嘛的
def find_sources(db: Session = Depends(get_db)):
  words = crud.queryAllWords(db)
  return {'data':words,'code': 200} # 不是200的情况怎么处理？？


if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8080) # 指定ip端口运行
