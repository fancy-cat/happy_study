# 中定义 Pydantic 模型，用于数据验证和序列化： 
# 干嘛的还不知道
from pydantic import BaseModel

class sourceBase(BaseModel):
    sourceType: str

class SourceFind(sourceBase):
    pass

class Source(sourceBase):
    id: int
    
    class Config:
        from_attributes = True