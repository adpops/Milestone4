from flask import Blueprint
from flask import render_template
from gymApp import db
import requests

mysql = db.getMySQL()
bp = Blueprint("admin", __name__, url_prefix="/admin/")

@bp.route('/location/', methods=['GET'])
def location ():
    cursor = mysql.connection.cursor()
    query = """ 
    CREATE TABLE IF NOT EXISTS Locations 
    (
        id                  INT unsigned NOT NULL AUTO_INCREMENT,
        branch_name         VARCHAR(150) NOT NULL,
        physical_address    VARCHAR(255) NOT NULL,
        postal_address      VARCHAR(255) NOT NULL,
        max_occupancy       INT NOT NULL,
        hours_of_operation  VARCHAR(255) NOT NULL,
        PRIMARY KEY         (id) 
    )    """

    post = cursor.execute(query)
    db.saveDb(mysql)
    db.closeDb(cursor)
    return "Hello World"
    # posts = cursor.fetchall()
    # return render_template('location.html', posts=posts)