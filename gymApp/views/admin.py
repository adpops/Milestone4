from flask import Blueprint
from flask import render_template
from gymApp import db
from gymApp.queries import admin
import requests

mysql = db.getMySQL()
bp = Blueprint("admin", __name__, url_prefix="/admin/")

@bp.route('/location/', methods=['GET'])
def location ():
    cursor = mysql.connection.cursor()
    query = admin.allTables()
    post = cursor.execute(query)
    db.saveDb(mysql)
    db.closeDb(cursor)
    return "Hello World"
    # posts = cursor.fetchall()
    # return render_template('location.html', posts=posts)