# 定义数据模型
from sqlalchemy import Column, Integer,VARCHAR
from app.database import Base

# 模型-学习来源
class Source(Base):
  __tablename__ = 'source_type' # 表名
  id = Column(Integer, primary_key=True)
  sourceType = Column(VARCHAR(45), primary_key=True)

  def __repr__(self): # 这个是干嘛的？
    return f"<Word id={self.id}, word={self.sourceType}>"
  
# 模型-单词
class Word(Base):
  __tablename__ = 'word'
  id = Column(Integer, primary_key=True)
  content = Column(VARCHAR(45), primary_key=True)

  def __repr__(self): 
    return f"<Word id={self.id}, word={self.content}>"
