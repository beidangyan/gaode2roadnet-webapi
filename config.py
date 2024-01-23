HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'road_db'
USERNAME = 'root'
PASSWORD = '!mysql789'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
