# 简介
基于flask和sqlalchemy的高德导航api获取指定点的路径经纬度坐标。
# 启动服务
1.运行命令 
```
flask db init
flask db migrate
flask db upgrade
```
2.在根路径下新建配置数据库的config.py文件
```
HOST = '127.0.0.1' # 数据库主机地址
PORT = '' # 数据库端口
DATABASE = '' # 数据库名称
USERNAME = '' # 数据库用户名
PASSWORD = '' # 数据库密码
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
GAODE_KEY = 'YOUR_KEY' # 把这里换成高德导航的webapi的key
```
3.运行app.py，可与[前端](https://github.com/beidangyan/gaode2roadnet-front)搭配使用。
