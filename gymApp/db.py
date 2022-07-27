from flask_mysqldb import MySQL
from gymApp import app

def setupDb():
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'admin'
    app.config['MYSQL_DB'] = 'testing'

def getMySQL():
    mysql = MySQL(app)
    return mysql

def saveDb(mysql):
    mysql.connection.commit()

def closeDb(cursor):
    cursor.close()

def createTables():
    mysql = getMySQL()
    query = """ CREATE  TABLE IF NOT EXISTS Locations (
        id INT  AUTOINCREMENT ,
        branch_name VARCHAR(150) NOT NULL ,
        physical_address VARCHAR(255) NOT NULL,
        postal_address VARCHAR(255) NOT NULL,
        max_occupancy INT NOT NULL,
        hours_of_operation VARCHAR(255) NOT NULL,
        PRIMARY KEY (id) )"""
    cursor = mysql.connection.cursor()
    cursor.execute(query)
