from flask import Flask
from app import views
from app import utils

app = Flask(__name__)
 
#url
app.add_url_rule('/base','base',views.base)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/faceapp','faceapp',views.faceapp)
app.add_url_rule('/faceapp/gender','gender',views.gender,methods=["GET","POST"])


#run
if __name__ == "__main__":
    app.run(debug=True)