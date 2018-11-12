from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime, timedelta

app=Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_USER']='host'
app.config['MYSQL_DATABASE_PASSWORD']= 'password'
app.config['MYSQL_DATABASE_DB']= 'dbmsdatabase'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

conn=mysql.connect()


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/vehicles', methods=['GET','POST'])
def info():
	
	cursor=conn.cursor()
	cursor.execute("SELECT * from vehicle")
	data=cursor.fetchall()	
	cursor.close()
	if request.method=='POST':
		vehid=request.form.get("vehicle_id")
		name=request.form.get("cust_name")
		dateofbirth=request.form.get("dob")
		number=request.form.get("phone")
		mail=request.form.get("email")
		aad=request.form.get("aadhar")
		add=request.form.get("address")
		cursor=conn.cursor()
		query= "insert into customer(cust_name,dob,vehicle_id,phone,email,aadhar,address) values(%s,%s,%s,%s,%s,%s,%s)"
		cursor.execute(query,(name,dateofbirth,vehid,number,mail,aad,add))
		conn.commit()
		return redirect('/vehicles/details')
	return render_template('bookingpage.html', data=data)


@app.route('/vehicles/details')
def show():
	today = datetime.today().strftime('%Y-%m-%d')
	del_date = datetime.now().today() + timedelta(days=7)
	new_price=0
	
	cursor=conn.cursor()
	query="select * from customer where cust_id in (select MAX(cust_id) from customer)"
	cursor.execute(query)
	dataC=cursor.fetchall()
	CRow=dataC[0]
	
	cursor.execute("select * from vehicle where vehicle_id = %s", CRow[2])
	dataV=cursor.fetchall()
	VRow=dataV[0]
	new_price= (VRow[3]+(0.18*VRow[3]))
	
	
	queryb="insert into booking(booked_date, del_date, vehicle_id, price, cust_id) values (%s,%s,%s,%s,%s)"
	cursor.execute(queryb,(today,del_date,CRow[2],new_price,CRow[0]))
	querybook="select * from booking where booking_id in ( select max(booking_id) from booking)"
	cursor.execute(querybook)
	dataB=cursor.fetchall()
	BRow=dataB[0]



	return render_template('booking_details.html', VRow=VRow, CRow=CRow, BRow=BRow)


@app.route('/vehicles/details/payment')
def pay():
	return render_template('payment.html')


@app.route('/login', methods=['GET','POST'])
def log():
	if request.method=='POST':
		empid= request.form.get("emp_id")
		eid=int(empid)
		pas=request.form.get("passwordd")
		cursor=conn.cursor()
		cursor.execute("select passwordd from login_credentials where emp_id=%s",eid)
		data=cursor.fetchall()
		for row in data:
			if row[0]==pas:
				return redirect('/vehicles')

	return render_template('loginpage.html')
		


	




if __name__ == '__main__':
	app.run(debug = True)



