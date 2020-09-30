from flask_sqlalchemy import SQLAlchemy
# 导入app工程文件
from app_ import app

# 连接数据库（格式：'mysql+pymysql://用户名:密码@端口号/数据库名'）
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/test'
# 取消警告
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# 数据库连接(生成一个数据库操作对象)
db = SQLAlchemy(app, )

