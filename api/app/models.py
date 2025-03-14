# 定义数据模型
from sqlalchemy import Column, Integer,VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# 模型-学习来源
class Source(Base):
  __tablename__ = 'source_type' # 表名
  id = Column(Integer, primary_key=True)
  source_type = Column(VARCHAR(45), primary_key=True)
  source_type_name = Column(VARCHAR(45), primary_key=True) # 初步发现，只有列出来的字段，才会从表里拿

  def __repr__(self): # 这个是干嘛的？
    return f"<Word id={self.id}, word={self.source_type_name}>"
  
# 模型-单词
class Word(Base):
  __tablename__ = 'word'
  id = Column(Integer, primary_key=True)
  word_name = Column(VARCHAR(45), primary_key=True)
  source_type = Column(VARCHAR(45), ForeignKey("source_type.source_type"))
  sources = relationship("Source", back_populates="words")
  def __repr__(self): 
    return f"<Word id={self.id}, word={self.word_name}, source_type={self.source_type}>"

Source.words = relationship('Word', order_by=Word.id, back_populates="sources") 
# Source.words是干嘛的
# back_populates用于在 SQLAlchemy 中定义双向关系，确保两个模型之间的关联属性能够互相引用和同步更新。
