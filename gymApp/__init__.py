import os
from flask import Flask
from flask_mysqldb import MySQL
# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__)

#     # app.config['MYSQL_HOST'] = 'localhost'
#     # app.config['MYSQL_USER'] = 'root'
#     # app.config['MYSQL_PASSWORD'] = 'admin'
#     # app.config['MYSQL_DB'] = 'flask'   
#     # mysql = MySQL(app)

#     # if test_config is None:
#     #     # load the instance config, if it exists, when not testing
#     #     app.config.from_pyfile('config.py', silent=True)
#     # else:
#     #     # load the test config if passed in
#     #     app.config.from_mapping(test_config)

#     # # ensure the instance folder exists
#     # try:
#     #     os.makedirs(app.instance_path)
#     # except OSError:
#     #     pass

#     # a simple page that says hello
#     @app.route('/hello')
#     def hello():
#         return 'Hello, World!'

#     return app

app = Flask(__name__)

from gymApp.views import auth, admin, member

from gymApp import db
db.setupDb()
# db.createTables()


app.register_blueprint(auth.bp)
app.register_blueprint(admin.bp)
app.register_blueprint(member.bp)
if __name__ == "__main__":
    app.run()