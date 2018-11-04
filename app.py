from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app=Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']= 'bangtan'
app.config['MYSQL_DATABASE_DB']= 'dbmsproject'
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
	return render_template('bookingpage.html', data=data)
		
	




if __name__ == '__main__':
	app.run(debug = True)



