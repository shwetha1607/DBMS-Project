from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app=Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']= 'bangtan'
app.config['MYSQL_DATABASE_DB']= 'dbmsminipro'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

conn=mysql.connect()


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/vehicles')
def info():
	cursor=conn.cursor()

	cursor.execute("SELECT * from vehicle")
	data=cursor.fetchall()
	return render_template('bookingpage.html', data=data)

@app.route('/vehicles/add')
def add():
	if request.method=="POST":
		custid=request.form['Cust_id']
		name=request.form['Name']
		dobb=request.form['DOB']
		phone=request.form['Phone']
		email=request.form['Email']
		addresss=request.form['Address']
		aaadhar=request.form['Adhaar']
		cursor=conn.cursor()
		sql= "insert into customer(customer_id,customer_name,dob,phone_no,email_id, aadhar, address) values (%s,%s,%s,%s,%s,%s,%s)"
		
		
		cursor.execute(sql,(custid,name,dobb,phone,email,aaadhar,addresss))
		conn.commit()
		return("nothing fucked")
	return render_template('bookingpage.html')




if __name__ == '__main__':
	app.run(debug = True)



