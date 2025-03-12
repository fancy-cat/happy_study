from app.database import SessionLocal
from sqlalchemy.orm import Session
from app.models import Word,Source
# 创建表（如果表不存在）
# Base.metadata.create_all(bind=engine)

# 查看所有来源
def querySourceList(db: Session):
  sources = db.query(Source).all()
  return sources

# 查询所有单词
def queryAllWords(db: Session):
  words = db.query(Word).all()
  for word in words:
    print(word)

  return words

# 插入单词
def insertWord(id,content,db):

  # 数据库操作
  new_word = Word(id=id,content=content)
  db.add(new_word)
  db.commit() # 提交更改
  db.refresh(new_word) #刷新对象，获取数据库生成的id
  print(f'插入的单词：{new_word}')


  return new_word

# 删除单词
def deleteWord(id,db):
  word = db.query(Word).filter(Word.id == id).first()
  if word:
    db.delete(word)
    db.commit()
    print('单词已删除')
  else:
    print('单词不存在')

  return word


