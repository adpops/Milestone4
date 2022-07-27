import os
from flask import Flask
from flask_mysqldb import MySQL


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