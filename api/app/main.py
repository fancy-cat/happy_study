# 定义数据模型
from sqlalchemy import Column, Integer,VARCHAR
from app.database import Base 
from app.words import queryAllWords
# 定义单词模型
class Word(Base):
  __tablename__ = 'duolinguo_words' # 表名
  id = Column(Integer, primary_key=True)
  content = Column(VARCHAR(45), primary_key=True)

  def __repr__(self): # 这个是干嘛的？
    return f"<Word id={self.id}, word={self.content}>"

if __name__ == "__main__":
  queryAllWords()