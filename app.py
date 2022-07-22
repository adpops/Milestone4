from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Member/Admin"

@app.route("/member")
def member():
    return "Sign up or Log In!"

@app.route("/member/SignUp")
def memberSignUp():
    return "Sign up a member!"

@app.route("/member/LogIn")
def memberLogIn():
    return "Enter Log In Info"

@app.route("/memberForm")
def memberForm():
    return "Enter Member Info"

@app.route("/memberBase")
def memberBase():
    return "Book an Appointment or update your info"

@app.route("/memberBase/Appointment")
def memberAppointment():
    return "Book an Appointment"

@app.route("/memberBase/Update")
def memberUpdate():
    return "Update your info"

@app.route("/admin")
def admin():
    return "Sign up or Log In!"

@app.route("/admin/LogIn")
def adminLogIn():
    return "Login to Admin"

@app.route("/adminBase")
def adminBase():
    return "View the list of members, appointments, locations, and employees"

@app.route("/adminBase/Members")
def adminMembers():
    return "View, update, or delete Members"

@app.route("/adminBase/Appointments")
def adminAppointments():
    return "View, update, or delete Appointments"

@app.route("/adminBase/Locations")
def adminLocations():
    return "View, update, or delete Locations"

@app.route("/adminBase/Employees")
def adminEmployees():
    return "View, update, or delete Employees"