模块解释：
<1> flask：安装 flask 及其依赖

<2> flask_sqlalchemy，pymysql：用Flask对象初始化SQLAlchemy，可以在flask项目中使用MTV模式进行各种对数据库的操作

<3> flask_migrate，flask_script：用于数据库的迁移操作，其中flask_script用来设置应用程序通过指令操作；flask_migrate导入数据库迁移类和数据库迁移指令类

<4> flask_session：对flask里面配合redis对session进行操作，存储或清除字段

<5> flask_blueprint：可以让Flask对象注册多个蓝图对象，相当于插入了blueprint的包装器，能够分割功能模块，能够更清晰的进行业务开发，而不是将所有的业务处理都写在一个views里

开始迁移数据库，在Terminal中执行以下三句指令：
注意： 执行语句之前，一定要将models里面的模型，导入到app.py中。否则执行第二句时就会报错。
① python manage.py db init  （只运行一次，为生成migrations文件夹，以便之后数据改变，版本迁移）
② python manage.py db migrate  （完成迁移）
③ python manage.py db upgrade  （更新数据库表格）

完成views.py中蓝图创建以及其他配置之后，到app.py中注册蓝图
from flask import Flask
app = Flask(__name__,template_folder='static/templates')
app.debug=True    

# 导入app1/views.py中创建的蓝图
from app1.views import app1
# 注册该蓝图
app.register_blueprint(app1, url_prefix='/app1')