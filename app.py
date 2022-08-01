from flask import Flask,  render_template, url_for, request, redirect
from flask_mysqldb import MySQL
import string
import re
app = Flask(__name__)

#DB Initialization
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'testing'
mysql = MySQL(app)

#User must create database on their local machine, and potentially modify the db commands

#To run, type flask run, or python app.py

# ------------------------------------------------------- HOME OF APP-------------------------------------------------------
#Base Page 
@app.route("/home", methods = ['GET'])
def home():
    return render_template('home.html')

# --------------------------------------------------------- Member Code/Routes ----------------------------------------------

#Route for adding a new member
@app.route("/member", methods = ['GET','POST'])
def member():
    if request.method == 'POST':
        #Get all information from the form
        fname = request.form['firstName']
        lname = request.form['lastName']
        birthday = request.form['birthday']
        sub = request.form['subscription']
        location = request.form['location']
        #Open the db
        cursor = mysql.connection.cursor()
        #Insert the form into the db
        cursor.execute('''INSERT INTO member (firstname, lastname, birthdate, sub_ID, location)
        VALUES(%s, %s, %s, %s, %s)''', (fname, lname, birthday, sub, location))
        #Get the last id
        mid = mysql.connection.insert_id()
        #Commit the changes
        mysql.connection.commit()
        #Close the cursor
        cursor.close()
        #Take the user to their unique home page
        return redirect(url_for('memberHome', mid = mid))
    elif request.method == 'GET':
        #Load the member form 
        return render_template('member.html')

#Unique Member home page
@app.route("/memberHome/<int:mid>")
def memberHome(mid):
    #Render the home page for each member
    return render_template('memberHome.html', val = mid)

#Allow a member to view their information
@app.route("/viewInfo/<int:mid>", methods = ['GET','POST'])
def viewInfo(mid):
    #Open db
    cursor = mysql.connection.cursor()
    #Get the specific member
    cursor.execute("SELECT * FROM member WHERE mid =  %s", (mid,))
    values = cursor.fetchall()
    mysql.connection.commit()
    cursor.close
    #Render the page with the member's information
    return render_template('viewInfo.html', memberList = values)

#Let a user update their information
@app.route('/updateInfo/<int:mid>', methods=['GET', 'POST'])
def updateInfo(mid):
    if request.method == 'POST':
        #Get information from the form
        fname = request.form['firstName']
        lname = request.form['lastName']
        birthday = request.form['birthday']
        sub = request.form['subscription']
        location = request.form['location']
        cur = mysql.connection.cursor()
        #Update the information
        cur. execute("UPDATE Member SET firstname=%s, lastname=%s, birthdate=%s, sub_id=%s , location=%s  WHERE mid=%s", (fname, lname, birthday,sub,location, mid))
        mysql.connection.commit()
        cur.close()
        #Take the user back to the view information page
        return redirect(url_for('viewInfo', mid = mid))  
    
    if request.method == 'GET':
        #Render the form for the user
        return render_template('updateInfo.html', mem=mid)

#Delete the information associated with your account
@app.route('/deleteInfo/<int:mid>', methods=['GET', 'POST'])
def deleteInfo(mid):
    #Delete the member information
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Member WHERE mid =  %s", (mid,))
    mysql.connection.commit()
    #Return to the home page
    return redirect(url_for('home'))  

@app.route('/bookAppointment/<int:mid>', methods =['GET','POST'])
def bookAppointment(mid):
    if request.method == 'POST':
        #Get form details
        userDetails = request.form
        name = userDetails['name'] 
        branch = userDetails['branch']
        date = userDetails['date']
        cur = mysql.connection.cursor()
        #Insert the information into appointments
        cur.execute("INSERT INTO Appointment(name, branch_id, date) VALUES(%s, %s, %s)", (name,branch,date))
        mysql.connection.commit()
        cur.close()
        #Take the user back to the view information page
        return redirect(url_for('memberHome', mid = mid))  
    if request.method == 'GET':
        #Render the form for the user
        return render_template('bookAppointment.html', val = mid)
# --------------------------------------------------------- Admin Code/Routes ----------------------------------------------
#Base admin route
@app.route('/admin')
def admin():
    return render_template('admin.html')

#Members
#Display all members for the admin
@app.route("/allMembers", methods = ['GET','POST'])
def memberList():
    #Post Request
    if(request.method == 'POST'):
        #Get all information from the form
        fname = request.form['firstName']
        lname = request.form['lastName']
        birthday = request.form['birthday']
        sub = request.form['subscription']
        location = request.form['location']
        #Open the db
        cursor = mysql.connection.cursor()
        #Insert the form into the db
        cursor.execute('''INSERT INTO member (firstname, lastname, birthdate, sub_ID, location)
        VALUES(%s, %s, %s, %s, %s)''', (fname, lname, birthday, sub, location))
        #Get the last id
        mid = mysql.connection.insert_id()
        #Commit the changes
        mysql.connection.commit()
        #Close the cursor
        cursor.close()
        #Redirect back to all Members
        redirect('/allMembers')
    #Get Request
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Member")
    mems = cur.fetchall()
    #Render all Members
    return render_template('allMembers.html', memberList = mems)

#Delete a specific member
@app.route('/deleteMember/<int:mid>', methods=['GET', 'POST'])
def deleteMember(mid):
    #Delete a specific member based on the member id
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Member WHERE mid =  %s", (mid,))
    mysql.connection.commit()
    return redirect('/allMembers')   

#Update a specific member's information (Used by admin)
@app.route('/updateMember/<int:mid>', methods=['GET', 'POST'])
def updateMember(mid):
    if request.method == 'POST':
        #Get information from form
        fname = request.form['firstName']
        lname = request.form['lastName']
        birthday = request.form['birthday']
        sub = request.form['subscription']
        location = request.form['location']
        cur = mysql.connection.cursor()
        #Open and execute the query to update the information for the user
        cur. execute("UPDATE Member SET firstname=%s, lastname=%s, birthdate=%s, sub_id=%s , location=%s  WHERE mid=%s", (fname, lname, birthday,sub,location, mid))
        mysql.connection.commit()
        cur.close()
        #Reload the list of all members
        return redirect(url_for('allMembers/',mid = mid))  
    
    if request.method == 'GET':
        #Render the form for a specific member
        return render_template('updateMember.html', mem=mid)

#Locations
@app.route('/allLocation', methods=['GET', 'POST'])
def allLocation():
    #Post Request
    if(request.method == 'POST'):
        #Request values in the form
        userDetails = request.form
        name = userDetails['branch_name']
        address = userDetails['address']
        maxOcc = userDetails['max_occupancy']
        hoursOp = userDetails['hours_of_operation']
        cur = mysql.connection.cursor()
        #Insert a new location
        cur.execute("INSERT INTO Locations(branch_name, address, max_occupancy, hours_of_operation) VALUES (%s, %s, %s, %s)"
        , (name, address, maxOcc, hoursOp,))
        mysql.connection.commit()
        cur.close()
        #Redirect back to all locations
        redirect('/allLocation')
    #Get Request
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Locations")
    locations = cur.fetchall()
    #Render all locations
    return render_template('allLocation.html', post=locations)

#Update a specific location
@app.route('/updateLocation/<int:bid>', methods=['GET', 'POST'])
def updateLocation(bid):
    if(request.method == 'POST'):
        #Request values in the form
        userDetails = request.form
        name = userDetails['branch_name']
        address = userDetails['address']
        maxOcc = userDetails['max_occupancy']
        hoursOp = userDetails['hours_of_operation']
        cur = mysql.connection.cursor()
        #Update the location
        cur.execute("UPDATE Locations SET branch_name = %s, address = %s, max_occupancy = %s, hours_of_operation = %s WHERE bid = %s"  
        , (name, address, maxOcc, hoursOp, bid))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('allLocation'))
    #Render the update form
    return render_template('updateLocation.html', post=bid)

#Delete a specific location
@app.route('/deleteLocation/<int:bid>', methods=['GET', 'POST'])
def deleteLocatation(bid):
    #Delete a specific Location
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Locations WHERE bid =  %s", (bid,))
    mysql.connection.commit()
    cur.close()
    #Render all the locations
    return redirect('/allLocation')   

#Equipment
@app.route('/allEquipment', methods=['GET', 'POST'])
#Show all equipment 
def allEquipment():
    if request.method == 'POST':
        #Request form details
        userDetails = request.form
        name = userDetails['name'] 
        status = userDetails['status']
        branch = userDetails['branch']
        cur = mysql.connection.cursor()
        #Insert the value into equipment
        cur.execute("INSERT INTO Equipment(name, status, branch_id) VALUES(%s, %s, %s)", (name,status,branch))
        mysql.connection.commit()
        cur.close()
        #Return to the equipment page
        return redirect('/allEquipment')
    else:
        #Display all equipment
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM equipment")
        equipments = cur.fetchall()
        return render_template('allEquipment.html', equipments=equipments)  

#Delete a specific piece of equipment
@app.route('/deleteEquipment/<int:eid>', methods=['GET', 'POST'])
def deleteEquipment(eid):
    #Delete equipment based on the eid
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Equipment WHERE eid =  %s", (eid,))
    mysql.connection.commit()
    #Return to the base equipement page
    return redirect('/allEquipment')

#Update a specific piece of equipment
@app.route('/updateEquipment/<int:eid>', methods=['GET', 'POST'])
def updateEquipment(eid):
    if request.method == 'POST':
        #Request form details
        name = request.form['name']
        status = request.form['status']
        branch = request.form['branch']
        cur = mysql.connection.cursor()
        #Update the value
        cur. execute("UPDATE Equipment SET name=%s, status=%s, branch_id=%s WHERE eid=%s", (name, status, branch,  eid))
        mysql.connection.commit()
        cur.close()
        #Return to base page
        return redirect ('/allEquipment')
    else:
        #Render the form to update locations
        return render_template('updateEquipment.html', equipment=eid)

#Employees
#List all employees
@app.route('/allEmployees', methods=['GET', 'POST'])
def allEmployees():
    if request.method == 'POST':
        #Get the form information
        userDetails = request.form
        firstname = userDetails['firstname'] 
        lastname = userDetails['lastname']
        birthdate = userDetails['birthdate']
        startdate = userDetails['startdate']
        branch = userDetails['branch']       
        cur = mysql.connection.cursor()
        #Insert the value
        cur.execute("INSERT INTO Employee(firstname, lastname, birthdate, startdate, branch_id) VALUES(%s, %s, %s, %s, %s)", (firstname,lastname,birthdate,startdate,branch))
        mysql.connection.commit()
        cur.close()
        #Return to the base employees folder
        return redirect('/allEmployees')
    else:
        #Render the page with all the employees
         cur = mysql.connection.cursor()
         resultValue = cur.execute("SELECT * FROM Employee")
         employee = cur.fetchall()
         return render_template('allEmployees.html', employees=employee) 

#Delete specific employees
@app.route('/deleteEmployee/<int:eid>', methods=['GET', 'POST'])
def deleteEmployee(eid):
    #Delete an employee based on the eid
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Employee WHERE eid =  %s", (eid,))
    mysql.connection.commit()
    return redirect('/allEmployees')  

#Update a specific employee
@app.route('/updateEmployee/<int:eid>', methods=['GET', 'POST'])
def updateEmployee(eid):
    if request.method == 'POST':
        #Get the form values
        userDetails = request.form
        firstname = userDetails['firstname'] 
        lastname = userDetails['lastname']
        birthdate = userDetails['birthdate']
        startdate = userDetails['startdate']
        branch = userDetails['branch']   
        cur = mysql.connection.cursor()
        #Update the db based on the values
        cur.execute("UPDATE Employee SET firstname=%s, lastname=%s, birthdate=%s, startdate=%s, branch_id=%s WHERE eid=%s", (firstname,lastname,birthdate,startdate,branch,eid,))
        mysql.connection.commit()
        cur.close()
        #Return the values
        return redirect(url_for('allEmployees'))
    else:
        #Render the form
        cur = mysql.connection.cursor()
        return render_template('updateEmployee.html', employees=eid)     

#Appointments
#Display all appointments
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

#Delete a specific appointment
@app.route('/deleteAppointment/<int:aid>', methods=['GET', 'POST'])
def deleteAppointment(aid):
    #Delete the value based on aid
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Appointment WHERE aid =  %s", (aid))
    mysql.connection.commit()
    #Render the home page containing all appointments
    return redirect('/allAppointments') 

#Update a specific appointment
@app.route('/updateAppointment/<int:aid>', methods=['GET', 'POST'])
def updateAppointment(aid):
    if request.method == 'POST':
        #Get form details
        userDetails = request.form
        name = userDetails['name'] 
        branch = userDetails['branch']
        date = userDetails['date']
        cur = mysql.connection.cursor()
        #Update the appointment information
        cur.execute("UPDATE Appointment SET name=%s, branch_id=%s, date=%s WHERE aid=%s", (name,branch,date, aid,))
        mysql.connection.commit()
        cur.close()
        #Render the list of appointments
        return redirect(url_for('allAppointments'))
    else:
        #Render the form for a specific appointment
        cur = mysql.connection.cursor()
        return render_template('updateAppointment.html', appointment=aid) 

#Stats page
@app.route('/stats', methods=['GET', 'POST'])
def stats():
    count = None
    colNames = None
    colName = None
    table = None
    cols = None

    # Division Query
    query = """
        SELECT DISTINCT x.firstname
        FROM Member AS x
        WHERE NOT EXISTS (
            SELECT *
            FROM Locations AS y
            WHERE NOT EXISTS (
                SELECT *
                FROM Member AS z
                WHERE (z.firstname = x.firstname)
                AND (z.location = y.bid)
            )
        );
    """
    cur = mysql.connection.cursor()
    cur.execute(query)
    posts = cur.fetchall()
    cur.close()

    # Nested Aggregation
    query = """
        SELECT member.sub_id, COUNT(*) 
        FROM MEMBER 
        WHERE Member.sub_id IN 
        (SELECT sid FROM Subscription) 
        GROUP BY member.sub_id;"""
    cur = mysql.connection.cursor()
    cur.execute(query)
    subs = cur.fetchall()
    cur.close()

    # Join Query
    query = """
        SELECT m.firstname, m.lastname, m.birthdate, m.location, s.price, s.termlength, s.renewaldate 
        FROM member m, subscription s 
        WHERE m.sub_id = s.sid;"""
    cur = mysql.connection.cursor()
    cur.execute(query)
    people = cur.fetchall()
    cur.close()

    if(request.method == "POST"):
        # Aggregation Query
        if('table_name' in request.form):
            tableName = request.form['table_name']
            query = "SELECT COUNT(*) FROM {};"
            cur = mysql.connection.cursor()
            cur.execute(query.format(tableName))
            count = cur.fetchone()
            cur.close()
        
        # Selection Query
        if('table' in request.form):
            tableName = request.form['table']
            query = "SELECT * FROM {};"
            cur = mysql.connection.cursor()
            cur.execute(query.format(tableName))
            table = cur.fetchall()
            cur.close() 
            query = "SHOW COLUMNS FROM {};"
            cur = mysql.connection.cursor()
            cur.execute(query.format(tableName))
            colNames = cur.fetchall()
            cur.close()

        # Projection Query
        if('column_name' in request.form and 'tableName' in request.form):
            tableName = request.form['tableName']
            colName = request.form['column_name']
            query = "SELECT " + colName + " FROM {};"
            cur = mysql.connection.cursor()
            cur.execute(query.format(tableName))
            cols = cur.fetchall()
            cur.close()

        return render_template('stats.html', post=posts, count=count, colNames=colNames, table=table, colName=colName, cols=cols, people=people, subs=subs)

    return render_template('stats.html', post=posts, people=people, subs=subs)

   
#Run code
if __name__ == '__main__':
    app.run(debug=True)