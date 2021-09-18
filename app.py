from flask import Flask, render_template, url_for, request

from flask_sqlalchemy import SQLAlchemy 


#import datetime
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'JSm21LKmsgghesgvSgbujnbv78bfhvkj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///root.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False



#initialize the db with app settings
db = SQLAlchemy(app)

#create the database model
class customer(db.Model):
     customer_id = db.Column(db.Integer,primary_key=True)
     first_Name = db.Column(db.String(80) , unique=True, nullable=False)
     last_Name = db.Column(db.String(80) , unique=True, nullable=False)
     email_Address = db.Column(db.String(80) , unique=True, nullable=False)
     contact_Number = db.Column(db.String(120) , unique=True, nullable=False)
     address = db.Column(db.String(80) , unique=True, nullable=False)
     user_Name = db.Column(db.String(80) , unique=True, nullable=False)
     password = db.Column(db.String(80) , unique=True, nullable=False)
     measurements = db.Column(db.String(120) , unique=True, nullable=False)

def __init__ (self, customerId, firstName, lastName, emailAddress, contactNumber, address, userName, password, measurements):
        self.customerId = customerId
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.contactNumber = contactNumber
        self.address = address
        self.userName = userName
        self.password =password
        self.measurements = measurements

#from app import db
#db.create_all()

@app.route('/', methods =['POST', 'GET'])
def customer ():
     if request.method == 'POST':
        
        
       new_entry = customer(customerId= request.form['customerId'], firstName=request.form['firstName'], 
       lastName=request.form['lastName'], emailAddress=request.form['emailAddress'], 
       contactNumber=request.form['contactNumber'], address=request.form['address'],
       userName=request.form['userName'], measurements=request.form['measurements'])
             
     try:
          db.session.add(new_entry)
          db.session.commit()
          return redirect('/')
     except:
          return "Error creating customer"

     else:
          return render_template("customer.html")    

class tailor(db.Model):
     tailor_id = db.Column(db.Integer,primary_key=True)
     first_Name = db.Column(db.String(80) , unique=True, nullable=False)
     last_Name = db.Column(db.String(80) , unique=True, nullable=False)
     email_Address = db.Column(db.String(80) , unique=True, nullable=False)
     contact_Number = db.Column(db.String(120) , unique=True, nullable=False)
     address = db.Column(db.String(80) , unique=True, nullable=False)
     user_Name = db.Column(db.String(80) , unique=True, nullable=False)
     password = db.Column(db.String(80) , unique=True, nullable=False)


def __init__ (self, tailorId, firstName, lastName, emailAddress, contactNumber,address, userName, password):
        self.tailorId = tailorId
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.contactNumber = contactNumber
        self.address = address
        self.password = password
        self.userName = userName


@app.route('/', methods =['POST', 'GET'])
def tailor ():
     if request.method == 'POST':
        
        
       new_entry = tailor(tailorId= request.form['tailorId'], firstName=request.form['firstName'], 
       lastName=request.form['lastName'], emailAddress=request.form['emailAddress'], 
       contactNumber=request.form['contactNumber'],address=request.form['address'],
       userName=request.form['userName'])
             
     try:
          db.session.add(new_entry)
          db.session.commit()
          return redirect('/')
     except:
          return "Error creating tailor"

     else:
          return render_template("tailor.html")    


       






     if __name__=="__main__":
          app.run(debug=True)


    

        


    
    

















