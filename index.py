from flask import Flask,render_template,request

from flask_sqlalchemy import SQLAlchemy #first you must be install flask-flask_sqlalchemy module
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_demo'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username_here:password_here@servername/database_name'
db = SQLAlchemy(app)

class Users(db.Model):
   user_id =db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   email = db.Column(db.String(80),unique=True,nullable=False)
   password = db.Column(db.String(80),nullable=False)
   gender = db.Column(db.String(20),nullable=False)




# render_template for read html file
#request is recieved data from html page form data

@app.route('/') #@app.route is a decorator is contain the url hit path
def page1():# no agrument requierd in Flask function
   return 'jai ho'

#in Flask python you can return anything like int string list dict etc.

@app.route('/raj')
def page2():
   a="<h1>Hello Beby</h1>"
   return f'i am Raj kushwaha R{a}'
@app.route('/index')
def index():
   a=[2,5,5,8]
   text = "Show Form"
   data={
      'a':a,
      'text':text,
   }
   return render_template('index.html',data=data)

@app.route('/signup',methods = ['POST', 'GET']) #for Form method Check
def sign_up():
   data=dict()
   if request.method == 'POST': #its check html page return POST OR NOT
      result = request.form
      data ={
      'name' :result.get('name'),
      'lname' :result.get('lname'),
      'gender' :result.get('gender'),
      }


   return render_template('signup.html',data=data)



# now we create a function for save aur form data

@app.route('/newaccount',methods = ['POST', 'GET'])
def sign_up_save():
   success=""
   if request.method == 'POST':
      name = request.form.get('name')
      email = request.form.get('email')
      gender = request.form.get('gender')
      password = request.form.get('password')
      u =Users(name=name,email=email,password=password,gender=gender)
      db.session.add(u)
      db.session.commit()
      success="data saved in database check your database"

   return render_template('newaccount.html',success=success)


app.run(debug=True)
