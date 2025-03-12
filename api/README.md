`requirements.txt`生成：`pip freeze > requirements.txt`展示出来的是所有包，会包含不必要的包
`pipreqs .`只会列出项目中使用到的包
运行项目：在 app 目录下运行这个`python -m app.main`

## 文件说明

- app
- crud----------操作数据库函数
- database------配置数据库的连接
- main----------接口函数
- models--------数据库模型
- schemas-------还不知道干嘛的，定义 respond 的吗？？
