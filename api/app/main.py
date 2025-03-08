# 定义数据模型
from sqlalchemy import Column, Integer,VARCHAR
from .database import Base,SessionLocal

# 定义任务模型
class Word(Base):
  __tablename__ = 'duolinguo_words' # 表名
  id = Column(Integer, primary_key=True)
  word = Column(VARCHAR(20), primary_key=True)
  tone = Column(Integer, primary_key=True)
  mean = Column(VARCHAR(100), primary_key=True)
  remark = Column(VARCHAR(100), primary_key=True)

  def __repr__(self): # 这个是干嘛的？
    return f"<Word id={self.id}, word={self.word}, tone={self.tone}, mean={self.mean}>"

# 创建表（如果表不存在）
# Base.metadata.create_all(bind=engine)

# 创建会话
db = SessionLocal()

# 查询所有任务
words = db.query(Word).all()
for word in words:
  print(word)

db.close()