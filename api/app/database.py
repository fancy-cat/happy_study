# 配置数据库的连接
from sqlalchemy import create_engine #sqlalchemyshi是ORM（对象关系映射）可以简化数据库操作
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库连接 URL（从环境变量读取
DATABAE_URL = 'mysql+pymysql://root:Wang@714211726@localhost/Japanese_study' #这个地址该怎么写？报错，连接不上

# 创建数据库引擎
engine = create_engine(DATABAE_URL)

# 创建本地会话类
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#声明基类
Base = declarative_base()

# # 测试连接
# def test_connection():
#   try:
#     engine.connect()
#     print("数据库连接成功！")
#   except Exception as e:
#     print(f"数据库连接失败: {e}")

# if __name__ == "__main__":
#   test_connection()