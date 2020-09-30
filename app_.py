# 导入flask模块
from flask import Flask

# 创建Flask的实例app，并设置共享网页文件夹templates的访问位置
app = Flask(__name__, template_folder='templates')
# 设置代码发生改变时，自动启动服务器
app.debug = True
# 以下两句先不写，蓝图创建后执行
from app.views import app1
print("import  views")
app.register_blueprint(app1, url_prefix='/')

