from flask import Blueprint
from flask import render_template
from gymApp import db
from gymApp.queries import admin
import requests

mysql = db.getMySQL()
bp = Blueprint("admin", __name__, url_prefix="/admin/")

@bp.route('/', methods=['GET'])
def allTables ():
    cursor = mysql.connection.cursor()
    queries = admin.allTables()
    queries = queries.split(';')
    for query in queries:
        cursor.execute(query)
        db.saveDb(mysql)
    db.closeDb(cursor)
    return "Hello World"
    # posts = cursor.fetchall()
    # return render_template('location.html', posts=posts)