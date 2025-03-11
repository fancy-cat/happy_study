from app.database import SessionLocal
from app.models import Word

# 创建表（如果表不存在）
# Base.metadata.create_all(bind=engine)

# 查询所有单词
def queryAllWords():
  # 创建会话
  db = SessionLocal() 

  words = db.query(Word).all()
  for word in words:
    print(word)

  # 关闭会话
  db.close()

  return words

# 插入单词
def insertWord():
  # 创建会话
  db = SessionLocal() 

  # 数据库操作
  new_word = Word(id=3,content='わたし')
  db.add(new_word)
  db.commit() # 提交更改
  db.refresh(new_word) #刷新对象，获取数据库生成的id
  print(f'插入的单词：{new_word}')

  # 关闭会话
  db.close()

  return new_word

# 删除单词
def deleteWord(id):
  # 创建会话
  db = SessionLocal() 

  word = db.query(Word).filter(Word.id == id).first()
  if word:
    db.delete(word)
    db.commit()
    print('单词已删除')
  else:
    print('单词不存在')

  # 关闭会话
  db.close()

  return word


