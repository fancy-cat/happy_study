# 定义数据模型
from sqlalchemy import Column, Integer,VARCHAR
from app.database import Base

# 单词模型
class Word(Base):
  __tablename__ = 'words' # 表名
  id = Column(Integer, primary_key=True)
  content = Column(VARCHAR(45), primary_key=True)

  def __repr__(self): # 这个是干嘛的？
    return f"<Word id={self.id}, word={self.content}>"
