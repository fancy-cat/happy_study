# from app.database import SessionLocal
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models import Word,Source
# 创建表（如果表不存在）
# Base.metadata.create_all(bind=engine)

# 查询所有来源及相应数据
def querySourceList(db: Session):
  result = (
    db.query(
      Source.source_type,
      Source.source_type_name,
      func.count(Word.id).label("word_count")
    )
    .join(Word, Source.source_type == Word.source_type, isouter=True) 
    .group_by(Source.source_type)
    .all()
  )
  # 如果返回的是 SQLAlchemy 的查询结果对象（如 Row 或模型实例），需要将其转换为字典
  #将 SQLAlchemy Row 对象转换为字典（不转这一道就会报错
  sources = [
    {"source_type": row.source_type, "word_count": row.word_count,"source_type_name": row.source_type_name}
    for row in result
  ]
  # isouter 左连接，确保没有来源的单词也能被查出来
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


