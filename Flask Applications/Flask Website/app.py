from flask import Flask, redirect, url_for, render_template

# To create the App
app = Flask(__name__)

# Creating a Home page
@app.route("/") #Home page
def home():
    return render_template("index.html", content="Testing")


# To run the app
if __name__ == "__main__":
    app.run(debug=True)