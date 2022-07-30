from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'testing'

mysql = MySQL(app)

@app.route('/findPeople', methods=['GET', 'POST'])
def findPeople():
    fname = request.form['firstname']
    query = """
        SELECT DISTINCT x.firstname
        FROM Member as x
        WHERE NOT EXISTS (
            SELECT *
            FROM Locations AS y
            WHERE NOT EXISTS (
                SELECT *
                FROM Member AS z
                WHERE (z.firstname = x.firstname)
                AND (z.location = y.branch_name)
            )
        )
        ;
    """
    cur = mysql.connection.cursor()
    cur.execute(query)
    people = cur.fetchall()
    
    return render_template('findPeople.html', post = people)
    

@app.route('/allLocation', methods=['GET', 'POST'])
def allLocation():
    if(request.method == 'POST'):
        userDetails = request.form
        name = userDetails['branch_name']
        address = userDetails['address']
        maxOcc = userDetails['max_occupancy']
        hoursOp = userDetails['hours_of_operation']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Locations(branch_name, address, max_occupancy, hours_of_operation) VALUES (%s, %s, %s, %s)"
        , (name, address, maxOcc, hoursOp,))
        mysql.connection.commit()
        cur.close()
        redirect('/allLocation')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Locations")
    locations = cur.fetchall()
    return render_template('allLocation.html', post=locations)

@app.route('/updateLocation/<int:bid>', methods=['GET', 'POST'])
def updateLocation(bid):
    if(request.method == 'POST'):
        userDetails = request.form
        name = userDetails['branch_name']
        address = userDetails['address']
        maxOcc = userDetails['max_occupancy']
        hoursOp = userDetails['hours_of_operation']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Locations SET branch_name = %s, address = %s, max_occupancy = %s, hours_of_operation = %s WHERE bid = %s"  
        , (name, address, maxOcc, hoursOp, bid))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('allLocation'))
    return render_template('updateLocation.html', post=bid)


@app.route('/deleteLocation/<string:bid>', methods=['GET', 'POST'])
def deleteLocatation(bid):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Locations WHERE bid =  %s", (bid,))
    mysql.connection.commit()
    cur.close()
    return redirect('/allLocation')      

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/allEquipment', methods=['GET', 'POST'])
def allEquipment():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name'] 
        status = userDetails['status']
        branch = userDetails['branch']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Equipment(name, status, branch_id) VALUES(%s, %s, %s)", (name,status,branch))
        mysql.connection.commit()
        cur.close()
        return redirect('/allEquipment')
    else:
         cur = mysql.connection.cursor()
         resultValue = cur.execute("SELECT * FROM equipment")
         equipments = cur.fetchall()
         return render_template('allEquipment.html', equipments=equipments)   


@app.route('/allAppointments', methods=['GET', 'POST'])
def allAppointments():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name'] 
        branch = userDetails['branch']
        date = userDetails['date']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Appointment(name, branch_id, date) VALUES(%s, %s, %s)", (name,branch,date))
        mysql.connection.commit()
        cur.close()
        return redirect('/allAppointments')
    else:
         cur = mysql.connection.cursor()
         resultValue = cur.execute("SELECT * FROM Appointment")
         appointment = cur.fetchall()
         return render_template('allAppointments.html', appointments=appointment)        


@app.route('/allEmployees', methods=['GET', 'POST'])
def allEmployees():
    if request.method == 'POST':
        userDetails = request.form
        firstname = userDetails['firstname'] 
        lastname = userDetails['lastname']
        birthdate = userDetails['birthdate']
        startdate = userDetails['startdate']
        branch = userDetails['branch']       
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Employee(firstname, lastname, birthdate, startdate, branch_id) VALUES(%s, %s, %s, %s, %s)", (firstname,lastname,birthdate,startdate,branch))
        mysql.connection.commit()
        cur.close()
        return redirect('/allEmployees')
    else:
         cur = mysql.connection.cursor()
         resultValue = cur.execute("SELECT * FROM Employee")
         employee = cur.fetchall()
         return render_template('allEmployees.html', employees=employee)         

 

@app.route('/deleteEquipment/<string:eid>', methods=['GET', 'POST'])
def deleteEquipment(eid):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Equipment WHERE eid =  %s", (eid))
    mysql.connection.commit()
    return redirect('/allEquipment')

@app.route('/deleteAppointment/<string:aid>', methods=['GET', 'POST'])
def deleteAppointment(aid):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Appointment WHERE aid =  %s", (aid))
    mysql.connection.commit()
    return redirect('/allAppointments')   

@app.route('/deleteEmployee/<string:eid>', methods=['GET', 'POST'])
def deleteEmployee(eid):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Employee WHERE eid =  %s", (eid))
    mysql.connection.commit()
    return redirect('/allEmployees')      

@app.route('/updateEquipment/<string:eid>', methods=['GET', 'POST'])
def updateEquipment(eid):
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        branch = request.form['branch']
        cur = mysql.connection.cursor()
        cur. execute("UPDATE Equipment SET name=%s, status=%s, branch_id=%s WHERE eid=%s", (name, status, branch,  eid[1]))
        mysql.connection.commit()
        cur.close()
        return redirect ('/allEquipment')
    else:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM equipment")
        equipments = cur.fetchall()
        return render_template('updateEquipment.html', equipment=equipments)

@app.route('/updateAppointment/<string:aid>', methods=['GET', 'POST'])
def updateAppointment(aid):
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name'] 
        branch = userDetails['branch']
        date = userDetails['date']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Appointment SET name=%s, branch_id=%s, date=%s WHERE aid=%s", (name,branch,date, aid[1]))
        mysql.connection.commit()
        cur.close()
        return redirect('/allAppointments')
    else:
         cur = mysql.connection.cursor()
         resultValue = cur.execute("SELECT * FROM Appointment")
         appointment = cur.fetchall()
         return render_template('updateAppointment.html', appointment=appointment) 

@app.route('/updateEmployee/<string:eid>', methods=['GET', 'POST'])
def updateEmployee(eid):
    if request.method == 'POST':
        userDetails = request.form
        firstname = userDetails['firstname'] 
        lastname = userDetails['lastname']
        birthdate = userDetails['birthdate']
        startdate = userDetails['startdate']
        branch = userDetails['branch']   
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Employee SET firstname=%s, lastname=%s, birthdate=%s, startdate=%s, branch_id=%s WHERE eid=%s", (firstname,lastname,birthdate,startdate,branch,eid[1]))
        mysql.connection.commit()
        cur.close()
        return redirect('/allEmployees')
    else:
         cur = mysql.connection.cursor()
         resultValue = cur.execute("SELECT * FROM Employee")
         employees = cur.fetchall()
         return render_template('updateEmployee.html', employees=employees)          


if __name__ == "__main__":
    app.run(debug=True)