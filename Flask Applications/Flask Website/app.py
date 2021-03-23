from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# To create the App
app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

#creating connection to database and flask app
db = SQLAlchemy(app)

# databse model
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Creating a Home page
@app.route("/") #Home page
def home():
    return render_template("index.html")

# View page
@app.route('/view')
def view():
    return render_template("view.html", values=users.query.all())
   
# login page
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email

        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Login Succesful")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))

        return render_template("login.html")

# User Login/Logout with POST,GET method
@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You are not Logged In!")
        return redirect(url_for("login"))

 #Logout from website  
@app.route('/logout')
def logout():
        flash("You have been logged out!", "info")
        session.pop("user", None)
        session.pop("email", None)
        return redirect(url_for("login"))

# To run the app
if __name__ == "__main__":
    db.create_all()       # Database creation, connection
    app.run(debug=True)   # Run the app
